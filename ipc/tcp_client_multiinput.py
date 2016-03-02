import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 9999))


while True :
	user_input = raw_input("Masukkan string yang akan dikirim ke server : ")
	sock.send(user_input)
	data_return = sock.recv(1000)
	print data_return
sock.close()
