import Adafruit_DHT
import time

SENSOR = Adafruit_DHT.DHT22
PIN = 4

while True:
	humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
	if humidity is not None and temperature is not None:
		print(f"Temp: {temperature:.1f}°C  Humidity: {humidity:.1f}%")
	else:
		print("Failed to retrieve Data from Sensor")
	time.sleep(2)
