#! /usr/bin/python3

import socket
import time
import threading
import sys
import user_thread

HOST_IP = "192.168.191.3"
HOST_PORT = 8001

host_addr = (HOST_IP, HOST_PORT)
print("Starting socket:TCP\n")
print("TCP server listening @ %s:%d" %(HOST_IP,HOST_PORT))
socket_tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_tcp.bind(host_addr)
socket_tcp.listen(5)
socks = []

def listen_handle():
    while True:
        socket_con,(client_ip,client_port) = socket_tcp.accept()
        socket_con.send("Connect Raspi server successed!".encode())
        socks.append(socket_con)
        thread = threading.Thread(target=user_handle,args=(socket_con,))
        thread.setDaemon(True)
        thread.start()

if __name__ =="__main__":
    # Set the listen thread
    thread = threading.Thread(target = listen_handle)    
    # set as daemon thread
    thread.setDaemon(True)
    thread.start()
    
    while True:
        cmd = input('''----------------------------
1:View current online number
2:...
----------------------------
enter your command:''')
        
        if cmd == "1":
                print("----------------------------")
                print("Current online number:%d"%(len(socks)))
                

 
