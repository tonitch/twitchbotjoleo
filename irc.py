import socket


class IRC:
    def __init__(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, chan, msg):
        self.irc.send(("PRIVMSG " + chan + " :" + msg + "\r\n").encode("utf-8"))

    def get_text(self):
        text = self.irc.recv(2048).decode("utf-8")

        if "PING" in text:
            print('PONG ' + text.split()[1] + '\r\n')
            self.irc.send(('PONG ' + text.split()[1] + '\r\n').encode("utf-8"))

        return text

    def connect(self, server, chan, botnick, passw):
        print("connecting to " + server)
        self.irc.connect((server, 6667))
        self.irc.send(("PASS " + passw + "\r\n").encode("utf-8"))
        self.irc.send(("NICK " + botnick + "\r\n").encode("utf-8"))
        self.irc.send(("JOIN " + chan + "\r\n").encode("utf-8"))
        print("connected")
