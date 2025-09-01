import Adafruit_DHT
import time
import json
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# ========================
# AWS IoT Configuration
# ========================

ENDPOINT = "a3etjvz66lbbgv-ats.iot.us-east-1.amazonaws.com"  # 🔁 Replace with your actual AWS IoT endpoint
CLIENT_ID = "raspiClient"
TOPIC = "raspi/temp"

# Cert/Key file paths (use exact file names from your folder)
ROOT_CA ="/home/azureazazel/python-projects/AmazonRootCA1.pem" 
PRIVATE_KEY ="/home/azureazazel/python-projects/RaspTempSensor.private.key" 
CERT_FILE ="/home/azureazazel/python-projects/RaspTempSensor.cert.pem"


SENSOR = Adafruit_DHT.DHT22
GPIO_PIN = 4

# ========================
# MQTT Client Setup
# ========================

client = AWSIoTMQTTClient(CLIENT_ID)
client.configureEndpoint(ENDPOINT, 8883)
client.configureCredentials(ROOT_CA, PRIVATE_KEY, CERT_FILE)
client.configureOfflinePublishQueueing(-1)  # Infinite queueing
client.configureDrainingFrequency(2)  # Draining: 2 Hz
client.configureConnectDisconnectTimeout(10)  # 10 sec
client.configureMQTTOperationTimeout(5)  # 5 sec

# ========================
# Main Loop
# ========================

try:
    print("Connecting to AWS IoT Core...")
    client.connect()
    print("✅ Connected!")

    while True:
        humidity, temperature = Adafruit_DHT.read(SENSOR, GPIO_PIN)

        if humidity is not None and temperature is not None:
            payload = {
                "temperature":float(temperature),
                "humidity": float(humidity),
                "timestamp": int(time.time()) 
            }

            client.publish(TOPIC, json.dumps(payload), 1)
            print(f"✅ Published: {payload}")
        else:
            print("⚠️ Failed to read sensor data.")

        time.sleep(60)  # Wait 60 seconds before next reading

except KeyboardInterrupt:
    print("❌ Stopped by user.")
    client.disconnect()
except Exception as e:
    print(f"❌ Error: {e}")
