import socket
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect( ('127.0.0.1', 6666) )

input_nama = raw_input('Nama mahasiswa : ')
input_nim = raw_input('NIM : ')
input_jurusan = raw_input('Jurusan : ')

dictionary_mhs = {
		"nama" : input_nama,
		"nim" : input_nim,
		"jurusan" : input_jurusan
	}

json_mhs = json.dumps(dictionary_mhs)
print "Client mrngirim : "+json_mhs
sock.send(json_mhs)
data = sock.recv(100)
print "Data yang diterima dari server : "+data
sock.close()
