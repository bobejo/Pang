class Player:
    def __init__(self, name, role, character):
        self.name = name
        self.role = role
        self.character = character
        self.hand = []
        self.health = 0
        self.weapon = None
        self.equipment = None

    def add_card(self, card):
        self.hand.append(card)

    def change_health(self, value):
        self.health += value
