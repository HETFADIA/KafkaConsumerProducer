from kafka import KafkaProducer
bootstrap_servers = 'localhost:9092'
topicName = 'orders'
producer = KafkaProducer(bootstrap_servers = bootstrap_servers,api_version=(0,11,5))
print("Producer made")

ack = producer.send(topicName, b'Hello World!!!!!!!!')
print("HI")
print(ack)
metadata = ack.get()
print(metadata.topic)
print(metadata.partition)
