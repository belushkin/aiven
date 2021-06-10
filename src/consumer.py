import os
import time
import schedule
import json

from db.pg import DB
from queues.broker import QueueConsumer


class Consumer():

    def __init__(self, db, queue):
        self.db = db
        self.queue = queue

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

        self.db.insert(
            os.environ['DB_TABLE_NAME'],
            {
                "http_response_time": gist['time'],
                "status_code": gist['code'],
                "page_content_exists": gist['exists']
            }
        )
        self.db.commit()
        return True

    def job(self) -> bool:
        print("Consuming...")
        for _ in range(2):
            raw_msgs = self.queue.poll(timeout_ms=1000)
            for tp, msgs in raw_msgs.items():
                for msg in msgs:
                    print("Received: {}".format(msg.value))
                    try:
                        self.insert(json.loads(msg.value.decode('utf-8')))
                        self.queue.commit()
                        return True
                    except ValueError:
                        return False


if __name__ == "__main__":
    consumer = Consumer(DB().db, QueueConsumer().consumer)

    schedule.every(
        int(os.environ['SCHEDULE_CONSUMER_POLL_PERIOD_IN_SECONDS'])
    ).seconds.do(consumer.job)

    while True:
        schedule.run_pending()
        time.sleep(1)
