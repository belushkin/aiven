import os
from json import dumps
from kafka import KafkaProducer, KafkaConsumer
from utils.singleton import Singleton

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class QueueProducer(metaclass=Singleton):
    """Kafka producer singleton incapsulates Kafka connection

    Returns
    -------
    KafkaProducer
        Object wich is connected to kafka topic and can produce messages
    """

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


class QueueConsumer(metaclass=Singleton):
    """Kafka consumer singleton incapsulates Kafka connection

    Returns
    -------
    KafkaConsumer
        Object wich is connected to kafka topic and can consume messages
    """

    def __init__(self):
        self.consumer = KafkaConsumer(
            os.environ['KAFKA_TOPIC'],
            auto_offset_reset=os.environ['KAFKA_OFFSET'],
            bootstrap_servers=os.environ['KAFKA_SERVER'],
            client_id=os.environ['KAFKA_CLIENT_ID'],
            group_id=os.environ['KAFKA_GROUP_ID'],
            security_protocol='SSL',
            ssl_cafile=f"{BASE_DIR}/certs/ca.pem",
            ssl_certfile=f"{BASE_DIR}/certs/service.cert",
            ssl_keyfile=f"{BASE_DIR}/certs/service.key"
        )
