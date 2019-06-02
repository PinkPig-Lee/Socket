import socket
import time
import sys

#Raspi's IP
SERVER_IP = '192.168.191.3'
SERVER_PORT = 8001

def SayHi_function(msg):
    print("%s" %msg)

print("Starting socket: TCP\n")
server_addr = (SERVER_IP, SERVER_PORT)
sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

if __name__ == "__main__":
    while True:
        try:
            print("Connecting to server",SERVER_IP,':',SERVER_PORT,'...')
            sock_tcp.connect(server_addr)
            break
        except Exception:
            print("Can't connect to server,try it later!")
            time.sleep(1)
            continue

    start_data = sock_tcp.recv(512).decode()   
    print("%s" %start_data)

    
    while True:
        try:
            cmd = input("Send your command:")
            if cmd == 'SayHi':
                sock_tcp.send(cmd.encode())
                Greet_data = sock_tcp.recv(512).decode()             # 函数本身会阻塞等待数据到来
                SayHi_function(Greet_data)
            elif cmd == 'q' or cmd == 'quit':
                sock_tcp.send(cmd.encode())
                bye_data = sock_tcp.recv(512).decode()
                print("%s" %bye_data)
                raise Exception
        except Exception:
            print("Connect break")
            sock_tcp.close()
            sock_tcp = None
            sys.exit(1)

            

