import time
import schedule
import json

from db.pg import DB
from queues.broker import Consumer

db = DB()
consumer = Consumer()


def action(gist):
    db.getConn().insert(
        'health_checker',
        {
            "http_response_time": gist['time'],
            "status_code": gist['code'],
            "page_content_exists": gist['exists']
        }
    )
    db.getConn().commit()


def job() -> bool:
    print("Consuming...")
    for _ in range(2):
        raw_msgs = consumer.getSelf().poll(timeout_ms=1000)
        for tp, msgs in raw_msgs.items():
            for msg in msgs:
                print("Received: {}".format(msg.value))
                try:
                    action(json.loads(msg.value.decode('utf-8')))
                    consumer.getSelf().commit()
                    return True
                except ValueError:
                    return False


if __name__ == "__main__":
    schedule.every(5).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)