import os
import time
import schedule
import json

from db.pg import DB
# from queues.broker import QueueConsumer

# consumer = Consumer()


class Consumer():

    def __init__(self, db):
        self.db = db

    def insert(self, gist) -> bool:
        """Inserts received gist from the message consumed from the Kafka topic
        to the DB

        If the gist is empty does not insert anything
        If the gist properties not exist does not insert anything

        Parameters
        ----------
        gist : dict, required
            Dictionary with required parameters:
            time: Http page response time
            code: Page response code
            exists: Result of the regex checking string on the page

        Raises
        ------
        psycopg3.Error
            Exception that is the base class of all other error exceptions.

        Returns
        -------
        bool
            The result of the action
        """
        if type(gist) is not dict:
            return False
        if 'time' not in gist:
            return False
        if 'code' not in gist:
            return False
        if 'exists' not in gist:
            return False

        print("v sachko")
        self.db.getConn().insert(
            os.environ['DB_TABLE_NAME'],
            {
                "http_response_time": gist['time'],
                "status_code": gist['code'],
                "page_content_exists": gist['exists']
            }
        )
        self.db.getConn().commit()
        return True


# def job() -> bool:
#     print("Consuming...")
#     for _ in range(2):
#         raw_msgs = consumer.getInstance().poll(timeout_ms=1000)
#         for tp, msgs in raw_msgs.items():
#             for msg in msgs:
#                 print("Received: {}".format(msg.value))
#                 try:
#                     insert(json.loads(msg.value.decode('utf-8')))
#                     consumer.getInstance().commit()
#                     return True
#                 except ValueError:
#                     return False


if __name__ == "__main__":
    consumer = Consumer(DB())
    print("aaa")
#     schedule.every(
#         int(os.environ['SCHEDULE_CONSUMER_POLL_PERIOD_IN_SECONDS'])
#     ).seconds.do(job)

#     while True:
#         schedule.run_pending()
#         time.sleep(1)
