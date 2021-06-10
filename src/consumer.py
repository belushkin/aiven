import time
import schedule

from db.pg import DB
from queues.broker import Consumer

db = DB()
consumer = Consumer()


def job():
    print("Consuming...")
    for _ in range(2):
        raw_msgs = consumer.getSelf().poll(timeout_ms=1000)
        for tp, msgs in raw_msgs.items():
            for msg in msgs:
                print("Received: {}".format(msg.value))
    consumer.getSelf().commit()


if __name__ == "__main__":

    # db.getConn().insert(
    #     "health_checker",
    #     {
    #         "http_response_time": 10,
    #         "status_code": 200,
    #         "page_content_exists": True
    #     }
    # )

    # db.getConn().commit()
    # print("Hello World")
    # print(db.getConn())
    # print(producer.getSelf())
    schedule.every(5).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
