from confluent_kafka import Producer
import socket

conf = {'bootstrap.servers': "localhost:9092",
        'client.id': socket.gethostname()}

producer = Producer(conf)
print("producer made")
producer.produce(topic='orders', key="key", value="value")
print("producer sent")
