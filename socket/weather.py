import socket
import threading

def load_weather(path,city):
    with open(path,'r',encoding='utf-8') as file:
        for item in file:
            if item.split(';')[0] == city:
                return item.split(';'[1:])
            return item.split(';')[1:]
        else:
            return False


def handle_clinet(conn,address):
    path = 'C:/Users/Student5/Downloads/python42/python42/socket/weather.txt'
    week = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday',' Friday', 'Saturday','Sunday']
    massege = 'Weather:\n'
    print(f'connect clinet {address}')
    conn.sendall('Hellou'.encode())
    while True:
        city=s.recv(1024).decode(encoding='utf-8')
        if city == False:
            break
        date = load_weather(path,city)
        if date == False:
            massege = 'City not found'
        for day in range(7):
            massege += f'{week[day]}:{date[day]}\n'
        conn.sendall(massege.encode())






host = '127.0.0.1'
port = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    s.bind((host,port))
    print(f'server{host} runer')     
    s.listen(5)
    while True:
        conn ,address = s.accept()
        threading.Thread(target=handle_clinet(conn,address)).start()
        