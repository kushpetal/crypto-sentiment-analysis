from kafka import KafkaConsumer, KafkaProducer

consumer = KafkaConsumer('crypto')
producer = KafkaProducer(bootstrap_servers='localhost:9092', api_version=(0,11,5))

def kafka_ingestion(topic, text_string):
    producer.send(topic, str.encode(text_string))



