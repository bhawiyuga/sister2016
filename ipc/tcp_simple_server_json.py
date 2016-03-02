import socket
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind( ('', 6666) )

sock.listen(10)

while True :
	conn,addr = sock.accept()
	data = conn.recv(100)
	dictionary_mhs = json.loads(data)
	print "Nama : "+dictionary_mhs["nama"]
	print "NIM : "+dictionary_mhs["nim"]
	print "Jurusan : "+dictionary_mhs["jurusan"]
	data = "OK"
	conn.send(data)
	conn.close()
