# Import library paho-mqtt
import paho.mqtt.client as mqtt

# Inisiasi mqtt client
mqttc = mqtt.Client("sub1", clean_session=False)

# Inisiasi callback function
def handle_message_masuk(mqttc, obj, msg):
    print "Message baru : "+msg.payload+" dengan topik "+msg.topic

#Registrasi callback function
mqttc.on_message = handle_message_masuk

# Buat koneksi ke broker
mqttc.connect("10.34.8.21", 1883)

# Subscribe dengan topik tertentu
mqttc.subscribe("filkom/sensor/suhu/1", qos=0)

# Looping subscriber
mqttc.loop_forever()
