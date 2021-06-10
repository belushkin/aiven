import time
import schedule

from queues.broker import Producer
from utils.checker import perform_measure

producer = Producer()


def job():
    print("Producing...")

    m = perform_measure("https://pypi.org/project/urllib3/")
    producer.getSelf().send(
        'health_checker_topic',
        key={'key': 1},
        value={'time': m.time, 'code': m.code, 'exists': m.exists}
    )
    producer.getSelf().flush()


if __name__ == "__main__":
    schedule.every(10).seconds.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
