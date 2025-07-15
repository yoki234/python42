import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    host = '127.0.0.1'
    port = 5000
    s.bind((host,port))  
    print(f'server{host} runer')                                   
    s.listen()
    conn, address = s.accept()
    while True:
        date = conn.recv(1024)
        if date == False:
            break
        conn.sendall(date)

