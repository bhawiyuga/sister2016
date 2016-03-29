# Import library Flask
from flask import Flask

# Inisialisasi objek Flask
app = Flask(__name__)

# Definisikan route URL dan function yang meng-handle route itu
@app.route('/', methods=['GET'])
def hello_world():
    return "Selamat Pagi!!!"

# Jalankan Flask web server
app.run(port=9999)
