# 🚀 Real-Time Crypto Transaction Tracker (AWS Kinesis + Redshift)

This project ingests **live Bitcoin transactions** using the **Blockchain.com WebSocket API**, streams them into **AWS Kinesis**, process the data with **AWS Lambda**, and loads it into **AWS Redshift** for querying and analysis.

## 📌 Features

- Live stream of BTC transactions in real time
- Kinesis Firehose delivery to S3 and Redshift
- SQL-ready tables for analysis

## 🧱 Architecture

```plaintext
[ Blockchain.com WebSocket ]
             ↓
[ Python Producer ]
             ↓
[ Kinesis Data Stream ]
             ↓
[ Kinesis Firehose ]
             ↓
[ Amazon S3 ] → [ Redshift COPY ]
             ↓
[ Live Queries + Dashboards ]
