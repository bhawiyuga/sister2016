import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer

# Buat fungsi
def tambah(a,b):
    return (a+b)

def kurang(a,b):
    return (a-b)

# Insiasi object xml rpc server
server = SimpleXMLRPCServer( ("", 6666) )
print "Listening on port 6666..."
# Registrasi fungsi di server
server.register_function(tambah, "add")
server.register_function(tambah, "tambah")
server.register_function(kurang, "kurang")
# Jalankan server
server.serve_forever()
