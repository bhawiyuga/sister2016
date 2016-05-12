import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer

input_port = input("Masukkan port server : ")

# Buat fungsi
def tambah(a,b):
    return (a+b)

def kurang(a,b):
    return (a-b)

# Insiasi object xml rpc server
server = SimpleXMLRPCServer( ("", input_port) )
print "Listening on port "+str(input_port)
# Registrasi fungsi di server
server.register_function(tambah, "add")
server.register_function(tambah, "tambah")
server.register_function(kurang, "kurang")
# Jalankan server
server.serve_forever()
