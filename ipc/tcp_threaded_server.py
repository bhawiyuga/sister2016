import socket
from threading import Thread

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 9999))
sock.listen(10)

class ServerThread(Thread):
	def __init__(self, connection, address):
		Thread.__init__(self)
		self.conn = connection
		self.addr = address

	def run(self):
		try :
			while True:
				data = conn.recv(1000)
				if data == "exit" :
					break
				else :
					data = "Hello "+data
					conn.send(data)
		except Exception :
			pass
		print "Connection closed"
		self.conn.close()
try :
	while True :
		conn, addr = sock.accept()
		t = ServerThread(conn, addr)
		t.start)(
except KeyboardInterrupt :
	sock.close()


