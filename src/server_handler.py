import socket
import selectors
import logging
import types
log = logging.getLogger(__name__)

sel = selectors.DefaultSelector()


def start_server(host_ip, port):
    log.info('Starting server on ip %s port %s', host_ip, port)
    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lsock.bind((host_ip, port))
    lsock.listen()
    log.info('Listening on %s', (host_ip, port))
    lsock.setblocking(False)
    sel.register(lsock, selectors.EVENT_READ, data=None)

    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection(key, mask)


def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print('accepted connection from', addr)
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)


def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            data.outb += recv_data
        else:
            log.info('Closing connection to %s', data.addr)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            log.info('Echoing %s to %s', repr(data.outb), data)
            sent = sock.send(data.outb)  # Should be ready to write
            data.outb = data.outb[sent:]
