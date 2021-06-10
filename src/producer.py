import os
import time
import schedule

from queues.broker import Producer
from utils.checker import perform_measure

producer = Producer()


def job():
    print("Producing...")

    measure = perform_measure(os.environ['HEALTH_URL'])
    producer.getInstance().send(
        os.environ['KAFKA_TOPIC'],
        key={'key': 1},
        value={
            'time': measure.time,
            'code': measure.code,
            'exists': measure.exists
        }
    )
    producer.getInstance().flush()


if __name__ == "__main__":
    schedule.every(
        int(os.environ['SCHEDULE_PRODUCER_CHECK_PERIOD_IN_SECONDS'])
    ).seconds.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
