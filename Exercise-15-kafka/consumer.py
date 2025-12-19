import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "electricity-prices",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

with open("output.json", "a") as f:
    for message in consumer:
        f.write(json.dumps(message.value) + "\n")
        print("Data saved to output.json")
