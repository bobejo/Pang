import random
import enum
import logging
import src.Cards as Cards
from src.Deck import StandardDeck
from src.Player import Player, Roles
from src.Character import Character


log = logging.getLogger(__name__)


class Game:
    def __init__(self, player_names):
        self.player_names = player_names
        self.deck = StandardDeck()
        self.active_player_index = 0
        self.players = self.create_players()
        self.sheriff = self.get_sheriff()
        self.active_player = self.sheriff


    @classmethod
    def start_game(cls, player_names):
        game_object = cls(player_names)
        game_object.draw_start_hand()
        return game_object

    def create_players(self):
        roles = [Roles.SHERIFF, Roles.OUTLAW, Roles.RENEGADE, Roles.DEPUTY, Roles.OUTLAW, Roles.OUTLAW, Roles.DEPUTY]
        amount_of_players = len(self.player_names)
        players = []
        if amount_of_players <= len(roles):
            roles = roles[:amount_of_players]
            random.shuffle(roles)
            i = 0
            for player, role in zip(self.player_names, roles):
                players.append(Player(name=player, role=role, character=self.get_character()))
                if role == Roles.SHERIFF:
                    self.active_player_index = i
                i += 1
            return players
        else:
            raise StartGameException('Maximum amount of players is 7 you entered {} players.'.format(amount_of_players))

    def draw_start_hand(self):
        for player in self.players:
            for i in range(player.health):
                player.add_cards(self.deck.take_top_card())
        log.info('Starting hand given to players')

    def get_sheriff(self):
        for player in self.players:
            if player.role == Roles.SHERIFF:
                return player

    def get_character(self):
        """
        Return the character chosen by the player
        :return:
        """
        # TODO fix function
        return Character(name='Billie the Kid', health=5)

    def switch_player(self):
        try:
            self.active_player = self.players[self.active_player_index+1]
            self.active_player_index += 1
        except IndexError:
            self.active_player_index = 0
            self.active_player = self.players[self.active_player_index]

    def get_possible_targets(self):
        """
        Returns all players the player can target with limited range cards
        :return:
        """
        player_index = self.players.index(self.active_player)
        player_range = 1
        if self.active_player.weapon:
            player_range = self.active_player.weapon.weapon_range
        if isinstance(self.active_player.equipment, Cards.ScopeCard):
            player_range += 1
        if player_range >= 3:
            return self.players.remove(self.active_player)
        possible_targets = []
        players = self.players.copy()
        players.extend(players)

        for i in range(player_index-player_range, player_index+player_range+1):
            possible_targets.append(players[i])
        possible_targets.remove(self.active_player)
        log.info('Possible targets are {}'.format(possible_targets))
        return possible_targets

    def use_card(self, card, target=None):
        if isinstance(card, Cards.PangCard):
            if isinstance(target, Player):
                if target in self.get_possible_targets():
                    log.info('Using pang! on {}'.format(target))
                    self.active_player.remove_card(card, self.deck)
                    if self.use_barrel(target):
                        return True
                    if self.use_miss_card(target):
                        return True
                    target.change_health(-1)
                else:
                    raise InvalidTargetException('Target {} is out of range.'.format(target))
            else:
                raise InvalidTargetException('Target {} is not a valid target'.format(target))
        elif isinstance(card, Cards.MissCard):
            if isinstance(target, Player):
                self.active_player.remove_card(card, self.deck)
                # TODO create miss card trigger
                log.info('Using miss card')

        elif isinstance(card, Cards.DrawCard):
            log.info('Using card {}, adding {} cards to hand.'.format(card, card.draw_amount))
            self.active_player.add_cards(self.deck.take_top_card(amount=card.draw_amount))
            self.active_player.remove_card(card, self.deck)
        elif isinstance(card, Cards.EquipmentCard):
            log.info('Equipping {}, with ability to {}'.format(card, card.ability))
            self.active_player.equipment = card
            self.active_player.remove_card(card)

        elif isinstance(card, Cards.WeaponCard):
            log.info('Equipping {}, setting range to {}'.format(card, card.weapon_range))
            self.active_player.weapon = card
            self.active_player.remove_card(card)

    def use_miss_card(self, target):
        for card in target.hand:
            if isinstance(card, Cards.MissCard):
                target.remove_card(card)
                return True
        return False

    def use_barrel(self, target):
        if isinstance(target.equipment, Cards.BarrelCard):
            barrel_card = self.deck.take_top_card()
            if barrel_card.suit == Cards.Suit.HEARTS:
                return True
        else:
            return False




class InvalidTargetException(Exception):
    pass


class StartGameException(Exception):
    pass
