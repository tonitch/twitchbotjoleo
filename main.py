import irc
import threading
import signal
import time
import sys


class readChat(threading.Thread):
    """
    read the chat and send response in function
    """
    def __init__(self):
        threading.Thread.__init__(self)
        self.next = True

    def run(self):
        while self.next:
            text = irc.get_text()
            print(text)

            if "PRIVMSG" in text and chan in text and text.split(":")[2].startswith("!"):
                if text.split(":")[2].startswith("!youtube"):
                    irc.send(chan, "Viens voir ma chaine youtube!\rhttps://www.youtube.com/channel/UCqI5rc5VspEwo5F9bMxDBSQ?view_as=subscriber")
                elif text.split(":")[2].startswith("!twitter"):
                    irc.send(chan, "Il ce passe quoi en ce moment ? go twitter ! \rhttps://twitter.com/Darkiller007")
                elif text.split(":")[2].startswith("!steam"):
                    irc.send(chan, "Viens jouer avec moi?!\rhttps://steamcommunity.com/id/JOLEO007/")

    def stop(self):
        self.next = False


class timerChat(threading.Thread):
    """
    set a timmer and send message over time
    """
    def __init__(self):
        threading.Thread.__init__(self)
        self.next = True
        self.count = 0

    def run(self):
        print("timer launched")
        while self.next:
            if self.count == 0:
                irc.send(chan, "[auto] Viens voir ma chaine youtube!: https://www.youtube.com/channel/UCqI5rc5VspEwo5F9bMxDBSQ?view_as=subscriber")
            elif self.count == 1:
                irc.send(chan, "[auto] Il ce passe quoi en ce moment ? go twitter !: https://twitter.com/Darkiller007")
            else:
                self.count = 0

            self.count += 1
            time.sleep(sleeptime*60)

    def stop(self):
        self.next = False


def executions():
    print("starting !")
    thread_chatReader.start()
    thread_chatTimer.start()


def closing(sig, frame):
    print("clossing !")
    irc.irc.send(("PART " + chan).encode("utf-8"))
    irc.irc.close()
    thread_chatReader.stop()
    thread_chatTimer.stop()
    sys.exit(0)


def main():

    irc.connect(server, chan, nick, passw)
    signal.signal(signal.SIGINT, closing)
    executions()


chan = "#joleo007"
server = "irc.chat.twitch.tv"
nick = "agentsergentchef"
passw = open("secretkey.txt", 'r').read()
sleeptime = 10

irc = irc.IRC()
thread_chatReader = readChat()
thread_chatTimer = timerChat()

if __name__ == "__main__":
    main()
