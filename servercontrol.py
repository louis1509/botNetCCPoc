#!/usr/bin/python3

import socket
import sys
import os
import threading
import queue

q = queue.Queue()
socketThread = []

def listener(lhost, lport, q):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    server.bind((lhost, lport))
    server.listen(100)


def main():
    if(len(sys.argv)<3):
        print('[!] Usage: \n[+] python3 ' + sys.argv[0] + ' <LHOST> <LPORT>\n[+] Ex : python3 ' + sys.argv[0] + ' 0.0.0.0 8080\n')
    else:
        try:
            lhost = sys.argv[1]
            lport = sys.argv[2]
            listener(lhost, lport, q)

if __name__ == "__main__":
    main()