from kafka import KafkaConsumer
consumer = KafkaConsumer('my_favorite_topic',group_id='group1',bootstrap_servers='localhost:9092',api_version=(0,11,5))
print("consumer made")
for msg in consumer:
    print (msg)
