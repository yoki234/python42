import socket
import threading
def incoming():
    while True:
        message = s.recv(1024).decode('utf-8')
        if message == False:
            break
        print('message',message)
host = '127.0.0.1'
port = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    s.connect((host,port))
    print('welcome to chat')


    threading.Thread(target = incoming).start() 
    while True:
        mes= input ('Input city')
        s.sendall(mes.encode())