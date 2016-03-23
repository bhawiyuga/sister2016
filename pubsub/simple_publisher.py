# Import library paho-mqtt
import paho.mqtt.client as mqtt

# Inisialisasi client
mqttc = mqtt.Client("pub1", clean_session=False)

# Buat koneksi ke broker
mqttc.connect("127.0.0.1", 1883)

# Publish message
mqttc.publish("filkom/sensor/suhu/1", payload="Selamat pagi", qos=0, retain=False)

