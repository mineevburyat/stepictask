import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(11)
while True:
	conn, addr = s.accept()
	while True:
		data = conn.recv(1024)
		st = str(data, encoding='utf-8').strip()
		print(st)		
		if not data:
			break
		if st = 'close':
			break
		conn.send(data)

	conn.close
