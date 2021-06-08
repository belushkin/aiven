import os
from json import dumps
from kafka import KafkaProducer
from utils.decorators import singleton


@singleton
class Producer():

    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=[os.environ['KAFKA_SERVER']],
            value_serializer=lambda x: dumps(x).encode('utf-8'),
            security_protocol='SSL'
        )

    def getSelf(self):
        return self.producer
