#Реализуйте погодное клиент-серверное приложение.
#Клиент обращается к серверу с указанием: страны и города. Сервер, получив запрос, возвращает погоду на неделю
#для данной местности. Используйте для реализации приложения механизмы многопоточности. Данные о погоде
#должны быть предопределенными и взяты из файла.

import socket
import threading


def handle_client(conn, address):
    print(f'Connect client {address}')
    while True:

        message = conn.recv(1024).decode(encoding='utf-8')
        if message == False:
            print('Disconnect')
            break
        for client in clients_list:
            if clients_list!=conn:
                client.sendall(message.encode())

host = '127.0.0.1'
port = 5000
clients_list = []

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    print(f'server {host} runer')
    s.listen(5)
    while True:
        conn, address = s.accept()
        clients_list.append(conn)
        threading.Thread(name='1', target=handle_client, args=(conn, address)).start()

