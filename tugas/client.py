import socket
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 9990))

list_operasi = ["penjumlahan", "pengurangan"]

while True :
	a = input("Masukkan angka ke-1 :  ")
	b = input("Masukkan angka ke-2 :  ")
	operasi = input("Masukkan operasinya : 1) Penjumlahan 2) Pengurangan : ")
	
	request_dict = {
		"a" : a,
		"b" : b,
		"tipe" : list_operasi[operasi-1]
	}

	req_json = json.dumps(request_dict)

	sock.send(req_json)
	data_return = sock.recv(1000)
	print data_return
sock.close()
