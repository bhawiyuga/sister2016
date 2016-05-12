import socket
from threading import Thread
import json
import xmlrpclib

list_rpcserver = ["http://localhost:6666/","http://localhost:6667/","http://localhost:6668/"]

list_conn_rpc = []

for rpc in list_rpcserver :
	proxy = xmlrpclib.ServerProxy(rpc)
	list_conn_rpc.append(proxy)

counter = 0
jumlah_server = len(list_rpcserver)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 9990))
sock.listen(10)

class ServerThread(Thread):
	def __init__(self, connection, address):
		Thread.__init__(self)
		self.conn = connection
		self.addr = address

	def run(self):
		global counter
		try :
			while True:
				data = conn.recv(1000)
				req_dict = json.loads(data)
				proxy = list_conn_rpc[counter]		
				if req_dict["tipe"] == "penjumlahan" :
					hasil = proxy.tambah(req_dict["a"], req_dict["b"])
				else :
					hasil = proxy.kurang(req_dict["a"], req_dict["b"])					
				print "a : ", req_dict["a"], " b : ", req_dict["b"], " operasi : ", req_dict["tipe"]
				conn.send("Hasil : "+str(hasil))
				counter = counter + 1
				if counter >= jumlah_server :
					counter = 0
		except Exception,e :
			print str(e)
		print "Connection closed"
		self.conn.close()
try :
	while True :
		conn, addr = sock.accept()
		t = ServerThread(conn, addr)
		t.start()
except KeyboardInterrupt :
	sock.close()


