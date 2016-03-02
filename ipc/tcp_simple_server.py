import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 9999))
sock.listen(10)


try :
	while True :
		conn, addr = sock.accept()
		data = conn.recv(1000)
		data = "Hello "+data
		conn.send(data)
except KeyboardInterrupt :
	sock.close()


