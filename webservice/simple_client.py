import httplib, urllib
import json

conn = httplib.HTTPConnection("localhost:9997")

# Data seluruh pegawai
def semua():
	conn.request("GET", "/pegawai")
	response = conn.getresponse()
	resp = response.read()
	#print resp
	data = json.loads(resp)
	for p in data :
		print p['nip'],p['nama'], p['alamat']
	#print response.read()

# Data pegawai dengan ID
def pegawai(id) :	
	conn.request("GET", "/pegawai/"+str(id))
	response = conn.getresponse()
	p = json.loads(response.read())
	print p['nip'], p['nama'], p['alamat']
	#print response.read()

def tambah_pegawai(nip="", nama="", alamat=""):
	headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
	params = urllib.urlencode({'nip': nip, 'nama': nama, 'alamat' : alamat})
	conn.request("POST", "/pegawai", params, headers)
	response = conn.getresponse()
	print response.read()

def update_pegawai(id, nip="", nama="", alamat=""):
	headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
	params = urllib.urlencode({'nip': nip, 'nama': nama, 'alamat' : alamat})
	conn.request("PUT", "/pegawai/"+str(id), params, headers)
	response = conn.getresponse()
	print response.read()

def delete_pegawai(id):
	conn.request("DELETE", "/pegawai/"+str(id))
	response = conn.getresponse()
	print response.read()

semua()
#pegawai(2)
#tambah_pegawai('678','Parjo', 'Kediri')
#update_pegawai(2, '910', 'Parjo2', 'Kediri')
#delete_pegawai(2)
