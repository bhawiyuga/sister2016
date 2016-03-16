import xmlrpclib

# Inisiasi remote client (xml rpc proxy)
proxy = xmlrpclib.ServerProxy("http://localhost:6666/")

a = 100
b = 10

# Jalankan fungsi tambah di server
hasil = proxy.add(a,b)
print a,"+",b,"=", hasil
# Jalankan fungsi tambah di server
hasil = proxy.tambah(a,b)
print a,"+",b,"=", hasil
# Jalankan fungsi kurang di server
hasil = proxy.kurang(a,b)
print a,"-",b,"=", hasil
