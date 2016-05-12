import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import json
# Import library paho-mqtt
import paho.mqtt.client as mqtt

list_pasien = []

list_poli = ["Umum", "Jantung", "Paru"]

# Inisialisasi client
mqttc = mqtt.Client()

# Buat koneksi ke broker
mqttc.connect("127.0.0.1", 1883)

# Buat fungsi
def tambah_pasien(pasien):
	pasien_dict = json.loads(pasien)
	list_pasien.append(pasien_dict)
	# Publish message
	nama_poli = list_poli[int(pasien_dict["poli"])-1]
	mqttc.publish("poli/"+nama_poli, payload=pasien, qos=0, retain=False)
	return "OK"

def lihat_pasien(nik):
	pasien = None
	for p in list_pasien :
		if p["nik"] == nik :
			pasien = p
			break
	if pasien is None :
		return "Pasien tidak ditemukan"
	else :
		return json.dumps(p)


# Insiasi object xml rpc server
server = SimpleXMLRPCServer( ("", 6666) )
print "Listening on port 6666..."
# Registrasi fungsi di server
server.register_function(tambah_pasien, "tambah_pasien")
server.register_function(lihat_pasien, "lihat_pasien")

# Jalankan server
server.serve_forever()
