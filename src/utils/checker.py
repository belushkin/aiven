import requests
from collections import namedtuple


def perform_measure(url=""):
    Measurement = namedtuple("Measurement", "time code exists")
    r = requests.get(url)

    exists = False
    if 'Project description' in r.text:
        exists = True

    return Measurement(r.elapsed.total_seconds(), r.status_code, exists)
