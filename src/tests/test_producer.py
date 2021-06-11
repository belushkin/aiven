from unittest.mock import patch, Mock

from producer import Producer
from collections import namedtuple


@patch('producer.perform_measure')
def test_producer_periodic_job_with_incorrect_message(mock_perform_measure):
    # given
    queue = Mock()

    Measurement = namedtuple("Measurement", "time code exists")
    mock_perform_measure.return_value = \
        Measurement(0.21, 200, True)

    producer = Producer(queue)

    # when
    producer.job()

    # then
    queue.send.assert_called_once()
    queue.flush.assert_called_once()
