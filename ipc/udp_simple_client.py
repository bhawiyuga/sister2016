import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto("Testing", ('127.0.0.1', 9999) )
data_return = sock.recv(1000)
print data_return
sock.close()
