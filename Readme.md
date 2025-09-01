# 📡 IoT-Based Temperature and Humidity Monitoring with Raspberry Pi and AWS

This project demonstrates a **complete end-to-end IoT data pipeline** using a Raspberry Pi and a DHT22 sensor. The system reads real-time temperature and humidity data, publishes it to **AWS IoT Core**, stores it in **DynamoDB**, and then uses **AWS Lambda** to export that data to **S3** on a schedule. The data is finally visualized using **Amazon QuickSight**.

---

## 🧠 Project Overview

- 🌡️ **Sensor**: DHT22 (for monitoring temperature and humidity)
- 🖥️ **Device**: Raspberry Pi (Python environment)
- ☁️ **Cloud Platform**: Amazon Web Services (AWS)
- 🔁 **Data Flow Pipeline**:
  1. Raspberry Pi reads sensor data using a Python script.
  2. Data is published to **AWS IoT Core** via MQTT.
  3. An **IoT Rule** sends the payload to **DynamoDB**.
  4. **AWS Lambda** function, triggered by **Amazon EventBridge** every hour, exports data from DynamoDB to **Amazon S3**.
  5. **Amazon QuickSight** is used to visualize sensor trends over time.

---

## 🔧 Technologies Used

| Component       | Service / Tool                    |
|----------------|------------------------------------|
| Sensor          | DHT22                             |
| Microcontroller | Raspberry Pi                      |
| Messaging       | AWS IoT Core (MQTT)               |
| Database        | DynamoDB                          |
| Serverless      | AWS Lambda                        |
| Scheduler       | Amazon EventBridge                |
| File Storage    | Amazon S3                         |
| Visualization   | Amazon QuickSight                 |
| Programming     | Python                            |

---

## 🔍 Architecture Diagram

```text
Raspberry Pi
   ↓ MQTT
AWS IoT Core (raspi/temp topic)
   ↓ IoT Rule
DynamoDB (RaspiSensorData)
   ↓ Lambda (every hour via EventBridge)
S3 Bucket (raspi_data_export.csv)
   ↓
Amazon QuickSight Dashboard
 ```
