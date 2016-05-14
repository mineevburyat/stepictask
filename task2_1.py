import socket
import threading

def listensock(socket):
    while True:
        conn, addr = socket.accept()
        while True:
            data = conn.recv(1024)
            st = str(data, encoding='utf-8').strip()
            if not data or st == 'close':
                print('close connection')
                break
            else:
                print(st)
                conn.send(data)
        conn.close()
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(11)
proc = [threading.Thread(target=listensock, name="proc"+str(i), args=[s]) for i in range(10)]
for p in proc:
    p.start()
