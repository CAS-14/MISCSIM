import socket
import selectors
import os

from core import log

class Server:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    def run(self):
        sel = selectors.DefaultSelector()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.listen()
        

class ServerGame:
    def __init__(self):
        pass

    self.tickrate = 60

    def run(self):
        pass
