import os
import time
import schedule

from queues.broker import QueueProducer
from utils.checker import perform_measure


class Producer():

    def __init__(self, queue):
        self.queue = queue

    def job(self):
        """Doing requests.get request to the selected url
        then take the result of the measurement and connects
        to the Kafka topic and produce the messages with the measurement
        results
        """
        print("Producing...")

        measure = perform_measure(os.environ['HEALTH_URL'])
        self.queue.send(
            os.environ['KAFKA_TOPIC'],
            key={'key': 1},
            value={
                'time': measure.time,
                'code': measure.code,
                'exists': measure.exists
            }
        )
        self.queue.flush()


if __name__ == "__main__":
    producer = Producer(QueueProducer().producer)

    schedule.every(
        int(os.environ['SCHEDULE_PRODUCER_CHECK_PERIOD_IN_SECONDS'])
    ).seconds.do(producer.job)

    while True:
        schedule.run_pending()
        time.sleep(1)
