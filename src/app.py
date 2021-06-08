from db.pg import DB

if __name__ == "__main__":

    db = DB()
    db.getConn().insert(
        "health_checker",
        {
            "http_response_time": 10,
            "status_code": 200,
            "page_content_exists": True
        }
    )

    db.getConn().commit()
    print("Hello World")

print("Ole")
