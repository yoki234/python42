import socket

host = '127.0.0.1'
port = 3000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    s.connect((host,port))
    welcom = s.recv().encode()
    print(welcom)
    while True:
        massage = input('input massage')
        if massage == False:
            break
        s.sendall(massage + '\n').encode()
        response = s.recv().decode()
        print(f'Response from {host}:{response}')
    print('desconnect')


