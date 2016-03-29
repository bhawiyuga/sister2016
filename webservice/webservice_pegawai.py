# Import library Flask
from flask import Flask, request, abort
import json

# Inisiasi objek Flask
app = Flask(__name__)

# Inisiasi data pegawai awal di dictionary. Bisa juga diambil dari DB
data_pegawai = [
        {
            "id" : 1,
            "nip" : "1234",
            "nama" : "Andi",
            "alamat" : "Malang"
        },
        {
            "id" : 2,
            "nip" : "5678",
            "nama" : "Joe",
            "alamat" : "Surabaya"
        }
    ]

# Definisikan rute dan fungsi
# REST WS untuk data seluruh pegawai
@app.route('/pegawai', methods=['GET'])
def index():
    str_pegawai = json.dumps(data_pegawai)
    return str_pegawai

# REST WS untuk data satu pegawai dengan ID tertentu
@app.route('/pegawai/<int:id>', methods=['GET'])
def get_pegawai(id):
    pegawai = None
    # Cari pegawai dengan ID tertentu dari dictionary pegawai
    for p in data_pegawai :
        if p["id"] == id :
            pegawai = p
            break
    # Kalau tidak ditemukan, return 404
    if pegawai is None :
        abort(404)
    # Kalau ditemukan return data pegawai tersebut
    str_pegawai = json.dumps(pegawai)
    return str_pegawai

# REST WS untuk create data pegawai 
@app.route('/pegawai', methods=['POST'])
def create_pegawai():
    # Dapatkan semua data dari parameter POST yang dikirim client
    nama = request.form.get('nama')
    nip = request.form.get('nip')
    alamat = request.form.get('alamat')
    # Auto increment ID pegawai
    id_terakhir = data_pegawai[-1]["id"]
    id_terakhir= id_terakhir+1
    # Buat data pegawai baru
    pegawai_baru = {
            "id" : id_terakhir,
            "nama" : nama,
            "nip" : nip,
            "alamat" : alamat
        }
    # Insert data pegawai baru ke dictionary data_pegawai
    data_pegawai.append(pegawai_baru)
    return "OK"

# REST WS untuk update data pegawai 
@app.route('/pegawai/<int:id>', methods=['PUT'])
def update_pegawai(id):
    # Dapatkan semua data dari parameter POST yang dikirim client
    nama = request.form.get('nama')
    nip = request.form.get('nip')
    alamat = request.form.get('alamat')
    # Cari pegawai dengan ID tertentu dari dictionary pegawai
    pegawai = None
    index = 0
    for p in data_pegawai :
        if p["id"] == id :
            pegawai = p
            break
        index = index+1
    # Kalau tidak ditemukan, return 404
    if pegawai is None :
        abort(404)
    # Kalau ditemukan kita update data pegawai tersebut
    pegawai["nip"] = nip
    pegawai["nama"] = nama
    pegawai["alamat"] = alamat
    # Update dictionary data_pegawai
    data_pegawai[index] = pegawai
    # Return data pegawai baru
    str_pegawai = json.dumps(pegawai)
    return str_pegawai

# REST WS untuk delete data pegawai 
@app.route('/pegawai/<int:id>', methods=['DELETE'])
def delete_pegawai(id):
    # Cari data pegawai yang akan dihapus
    pegawai = None
    for p in data_pegawai :
        if p["id"] == id :
            pegawai = p
            break
    # Jika pegawai tidak ditemukan return 404
    if pegawai is None :
        abort(404)
    # Jika ditemukan, hapus data pegawai tersebut
    data_pegawai.remove(pegawai)
    # Return informasi Deleted
    return "Deleted"

app.run(port=9997, debug=True)
