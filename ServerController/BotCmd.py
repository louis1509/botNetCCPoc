import threading
import queue
import time
import os

class BotCmd(threading.Thread):
    def __init__(self, qv2, socketThread):
        threading.Thread.__init__(self)
        self.q = qv2
        self.socketThread = socketThread

    def run(self):
        while True:
            sendCmd = str(input("Bot command > "))
            if(sendCmd ==""):
                pass
            elif(sendCmd == 'exit'):
                for i in range(len(self.socketThread)):
                    time.sleep(0.1)
                    self.q.put(sendCmd)
                time.sleep(5)
                os._exit(0)
            else:
                print("[+] Sending command: " + sendCmd + " to " + str(len(self.socketThread)) + " bots")
                for i in range(len(self.socketThread)):
                    time.sleep(0.1)
                    self.q.put(sendCmd)
                