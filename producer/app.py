import json
import boto3
import websocket
from config import AWS_REGION, KINESIS_STREAM_NAME, BLOCKCHAIN_WS_URL

# Initialize Kinesis client
kinesis = boto3.client("kinesis", region_name=AWS_REGION)

def send_to_kinesis(payload: dict):
    try:
        kinesis.put_record(
            StreamName=KINESIS_STREAM_NAME,
            Data=json.dumps(payload),
            PartitionKey=str(payload.get("x", {}).get("hash", "unknown"))
        )
        print(f"✔ Sent tx {payload['x']['hash']} to Kinesis")
    except Exception as e:
        print(f"❌ Failed to send to Kinesis: {e}")

def on_message(ws, message):
    try:
        data = json.loads(message)
        print(json.dumps(data, indent=4))
        #send_to_kinesis(data)
    except Exception as e:
        print(f"❌ Error processing message: {e}")

def on_error(ws, error):
    print(f"WebSocket error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("🔌 WebSocket closed")

def on_open(ws):
    # Subscribe to unconfirmed BTC transactions
    msg = json.dumps({"op": "unconfirmed_sub"})
    ws.send(msg)
    print("📡 Subscribed to unconfirmed transactions")

def run():
    ws = websocket.WebSocketApp(
        BLOCKCHAIN_WS_URL,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.run_forever()

if __name__ == "__main__":
    run()
