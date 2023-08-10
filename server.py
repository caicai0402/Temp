# Problem 3 - Inheritance
# Write some examples with inheritance code here.

# reference: https://shengyu7697.github.io/python-tcp-socket/

import socket

class UDPSocket():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_message(self, message, addr):
        self.socket.sendto(message.encode(), addr)
        print(f"Message \"{message}\" has been sent to {addr} successfully!")

    def receive_message(self):
        message, addr = self.socket.recvfrom(1024)
        message = message.decode()
        print(f"Message \"{message}\" has been received from {addr} successfully!")
        return message, addr

class UDPServer(UDPSocket):
    def __init__(self, host, port):
        super().__init__(host, port)

    def start(self):
        self.socket.bind((self.host, self.port))
        while True:
            indata, addr = self.receive_message()
            self.send_message("echo: " + indata, addr)
            if indata == "close":
                break
        self.socket.close()

class UDPClient(UDPSocket):
    def __init__(self, host, port):
        super().__init__(host, port)

    def start(self):
        while True:
            outdata = input()
            self.send_message(outdata, (self.host, self.port))
            indata, arrd = self.receive_message()
            if outdata == "close":
                break
        self.socket.close()



server = UDPServer("0.0.0.0", 9999)
server.start()
