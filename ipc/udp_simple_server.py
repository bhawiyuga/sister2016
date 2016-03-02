import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 9999))

try :
	while True :
		data, addr = sock.recvfrom(1000)
		data = "Hello "+data
		sock.sendto(data, addr)
except KeyboardInterrupt :
	sock.close()


