# 📡 IoT-Based Temperature and Humidity Monitoring with Raspberry Pi and AWS

This project demonstrates a complete IoT pipeline using a Raspberry Pi and a DHT22 sensor to monitor temperature and humidity data, publish it to AWS IoT Core, store it in DynamoDB, export to S3 using a Lambda function, and visualize it in Amazon QuickSight.

---

## 🧠 Project Overview

- 🌡️ **Sensor**: DHT22 (Temperature & Humidity)
- 🖥️ **Device**: Raspberry Pi
- ☁️ **Cloud Platform**: AWS
- 🔁 **Data Flow**:
  1. Raspberry Pi reads sensor data.
  2. Publishes to AWS IoT Core using MQTT.
  3. IoT Rule writes data into **DynamoDB**.
  4. **AWS Lambda** (triggered by **EventBridge**) exports data to **S3** every hour.
  5. Data is visualized in **Amazon QuickSight**.

---

## 🔧 Technologies Used

| Component       | Service / Tool                    |
|----------------|------------------------------------|
| Sensor          | DHT22                             |
| Microcontroller | Raspberry Pi                      |
| Messaging       | AWS IoT Core (MQTT)               |
| Storage         | DynamoDB                          |
| Serverless      | AWS Lambda                        |
| Scheduler       | Amazon EventBridge                |
| File Storage    | Amazon S3                         |
| Visualization   | Amazon QuickSight                 |
| Language        | Python                            |

---

---


Raspberry Pi
   ↓ MQTT
AWS IoT Core (raspi/temp topic)
   ↓ Rule
DynamoDB (RaspiSensorData)
   ↓ Lambda (every hour)
S3 Bucket (raspi_data_export.csv)
   ↓
QuickSight Dashboard
