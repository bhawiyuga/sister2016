import Pyro4

# Inisiasi remote object
penghitung = Pyro4.Proxy("PYRO:penghitung@127.0.0.1:9555")
penghitungdua = Pyro4.Proxy("PYRO:penghitungdua@127.0.0.1:9555")

a = 100
b = 10

# Jalankan method tambah di remote object penghitung
hasil = penghitung.tambah(a,b)
print a,"+",b,"=", hasil
# Jalankan method kurang di remote object penghitung
hasil = penghitung.kurang(a,b)
print a,"-",b,"=", hasil

hasil = penghitung.bagi(a,b)
print a,"/",b,"=", hasil

hasil = penghitung.kali(a,b)
print a,"*",b,"=", hasil
