# Import library paho-mqtt
import paho.mqtt.client as mqtt
import sys

poli = "Umum"
if len(sys.argv) > 1 :
	poli = sys.argv[1]

# Inisiasi mqtt client
mqttc = mqtt.Client()

# Inisiasi callback function
def handle_message_masuk(mqttc, obj, msg):
    print "Message baru : "+msg.payload+" dengan topik "+msg.topic

#Registrasi callback function
mqttc.on_message = handle_message_masuk

# Buat koneksi ke broker
mqttc.connect("127.0.0.1", 1883)

# Subscribe dengan topik tertentu
mqttc.subscribe("poli/"+poli, qos=0)

# Looping subscriber
mqttc.loop_forever()
