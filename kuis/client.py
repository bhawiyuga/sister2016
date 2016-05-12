import json
import xmlrpclib

# Inisiasi remote client (xml rpc proxy)
proxy = xmlrpclib.ServerProxy("http://localhost:6666/")

list_poli = ["Umum", "Jantung", "Paru"]

try : 
	while(True) :
		print ""
		print "Sistem Informasi Pasien"
		print "1. Masukkan data pasien"
		print "2. Lihat data pasien"
		print "3. Keluar"
		operasi = input("Pilih operasi : ")
		if operasi == 1 :
			print ""
			print "Masukkan data pasien"
			nik = raw_input("NIK : ")
			nama = raw_input("Nama : ")
			alamat = raw_input("Alamat : ")
			penyakit = raw_input("Penyakit : ")
			poli = input("Pilihan poli : 1) Umum, 2) Jantung, 3) Paru : ")
			pasien_baru = {
				"nik" : nik,
				"nama" : nama,
				"alamat" : alamat,
				"penyakit" : penyakit,
				"poli" : poli
			}
			pasien_baru_json = json.dumps(pasien_baru)
			proxy.tambah_pasien(pasien_baru_json)
		elif operasi == 2 :
			print ""
			nik = raw_input("NIK Pasien : ") 
			print "Data Pasien dengan NIK "+ nik			
			try :
				pasien_json = proxy.lihat_pasien(nik)
				p = json.loads(pasien_json)
				print "Nama : ",p["nama"]
				print "Alamat : ",p["alamat"]
				print "Penyakit : ",p["penyakit"]
				print "Poli : ", list_poli[int(p["poli"])-1]	
			except :
				print pasien_json 
		else :
			print ""
			print "Keluar dari program"
			break
except KeyboardInterrupt :
	print "Keluar dari program"