import pandas as pd
from kafka import KafkaProducer, KafkaConsumer
from time import sleep
from json import dumps
import json

ip_address =  "localhost:9092"
topic = "test"

producer = KafkaProducer(bootstrap_servers=[ip_address],
                         value_serializer=lambda x: dumps(x).encode('utf-8'))
# Sending Dummy Data
producer.send(topic, value={"name": "John", "age": 30})

# Sending Data from CSV


print("Ok")