import os
import sys
from json import dumps
from kafka import KafkaProducer
from utils.decorators import singleton
# from app import BASE_DIR


@singleton
class Producer():

    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.realpath(__file__))
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
