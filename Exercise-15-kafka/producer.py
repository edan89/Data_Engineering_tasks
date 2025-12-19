import json
import time
from kafka import KafkaProducer

# Initialize Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

TOPIC = 'electricity-prices'

def run_producer():
    with open('electricity-prices.json', 'r') as f:
        data = json.load(f)
        prices = data['prices']

    last_sent_time = None

    # Iterating through the data to simulate real-time updates
    for entry in reversed(prices):  # reversed to send oldest to newest
        current_time = entry['startDate']
        
        # Logic: Send if the timestamp is different from the last one processed
        if current_time != last_sent_time:
            producer.send(TOPIC, entry)
            print(f"Sent: {current_time} - Price: {entry['price']}")
            last_sent_time = current_time
            # Small sleep to simulate streaming
            time.sleep(1) 
    
    producer.flush()

if __name__ == "__main__":
    run_producer()