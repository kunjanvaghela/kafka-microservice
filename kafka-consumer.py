import pandas as pd
from kafka import KafkaProducer, KafkaConsumer
from time import sleep
from json import dumps
import json

ip_address =  "localhost:9092"
topic = "test"

consumer = KafkaConsumer(topic,
                         bootstrap_servers=[ip_address],
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

# Reading Data
for c in consumer:
    print(c)
    print(c.value)

print("Ok")