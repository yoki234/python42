#Реализуйте клиент — серверное приложение, позволяющее обмениваться сообщениями в формате один к
#одному. Для начала общения необходимо установить
#соединение. После соединение используется текстовый
#формат. В беседе участвуют только два человека. После
#завершения беседы сервер переходит к ожиданию нового
#участника разговора.

import socket
def handle_client(conn,adderson ):
    print(f'connect clinet {adderson}')
    conn.sendall('Hellou')
    while True:
        date=conn.recv(1024).encode()
        if date == False:
            print('Disconnect ')
            break
        print(f' massag from{adderson}:{date}')
        response = input('Input respone to cliner')
        conn.sendall(response).encode()

host = '127.0.0.1'
port = 3000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    s.connect((host,port))
    print(f'server{host} runer')     
    s.sendall(3)  
    while True:
        conn ,adderson  = s.accept()
        handle_client(conn,adderson)
        print('ожидание следущего клиента')