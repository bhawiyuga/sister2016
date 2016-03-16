import Pyro4

# Definisikan class beserta methodnya
class Penghitung(object) :
    def tambah(self, a,b):
        return (a+b)

    def kurang(self, a,b):
        return (a-b)

    def kali(self, a,b):
        return (a*b)

    def bagi(self, a,b):
        return (a/b)

# Inisiasi object Pyro4 daemon, parameter : IP dan Port
server_daemon = Pyro4.Daemon(host="", port=9555)

# Inisiasi object Penghitung
penghitung = Penghitung()
penghitung_dua = Penghitung()
# Jalankan server, parameter : dictionary object, nameserver, daemon
Pyro4.Daemon.serveSimple(
		{
			penghitung: "penghitung",
			penghitung_dua : "penghitungdua"
		},
		ns = False,
		daemon = server_daemon)
