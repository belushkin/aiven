from db.pg import DB
from queues.broker import Producer
from utils.checker import perform_measure


if __name__ == "__main__":

    db = DB()
    producer = Producer()

    # db.getConn().insert(
    #     "health_checker",
    #     {
    #         "http_response_time": 10,
    #         "status_code": 200,
    #         "page_content_exists": True
    #     }
    # )

    # db.getConn().commit()
    print("Hello World")
    print(db.getConn())
    print(producer.getSelf())
    print(perform_measure("https://pypi.org/project/schedule/"))

print("Ole")
