import os
from json import dumps
from kafka import KafkaProducer, KafkaConsumer
from utils.decorators import singleton

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


@singleton
class Producer():

    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=os.environ['KAFKA_SERVER'],
            security_protocol="SSL",
            ssl_cafile=f"{BASE_DIR}/certs/ca.pem",
            ssl_certfile=f"{BASE_DIR}/certs/service.cert",
            ssl_keyfile=f"{BASE_DIR}/certs/service.key",
            value_serializer=lambda v: dumps(v).encode('ascii'),
            key_serializer=lambda v: dumps(v).encode('ascii')
        )

    def getSelf(self):
        return self.producer


@singleton
class Consumer():

    def __init__(self):
        self.consumer = KafkaConsumer(
            'health_checker_topic',
            auto_offset_reset='earliest',
            bootstrap_servers=os.environ['KAFKA_SERVER'],
            client_id='health-client-1',
            group_id='health-group',
            security_protocol='SSL',
            ssl_cafile=f"{BASE_DIR}/certs/ca.pem",
            ssl_certfile=f"{BASE_DIR}/certs/service.cert",
            ssl_keyfile=f"{BASE_DIR}/certs/service.key"
        )

    def getSelf(self):
        return self.consumer
