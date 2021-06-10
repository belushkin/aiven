from unittest.mock import Mock
from consumer import Consumer
from collections import namedtuple


def test_consumer_insert_when_it_receives_empty_dict():
    # given
    consumer = Consumer(Mock(), Mock())

    # when
    result = consumer.insert({})

    # then
    assert result is False


def test_consumer_insert_when_it_receives_dict_without_time_property():
    # given
    consumer = Consumer(Mock(), Mock())

    # when
    result = consumer.insert({'code': 200, 'exists': True})

    # then
    assert result is False


def test_consumer_insert_when_it_receives_dict_without_code_property():
    # given
    consumer = Consumer(Mock(), Mock())

    # when
    result = consumer.insert({'time': 0.1, 'exists': True})

    # then
    assert result is False


def test_consumer_insert_when_it_receives_dict_without_exists_property():
    # given
    consumer = Consumer(Mock(), Mock())

    # when
    result = consumer.insert({'time': 0.1, 'code': 200})

    # then
    assert result is False


def test_consumer_insert_when_it_receives_not_dict():
    # given
    consumer = Consumer(Mock(), Mock())

    # when
    result = consumer.insert(False)

    # then
    assert result is False


def test_consumer_insert_when_it_receives_correct_dict():
    # given
    db = Mock()
    consumer = Consumer(db, Mock())

    # when
    result = consumer.insert({'time': 0.1, 'code': 200, 'exists': True})

    # then
    assert result is True
    db.commit.assert_called_once()
    db.insert.assert_called_once()


def test_consumer_periodic_job_with_correct_message():
    # given
    db = Mock()
    queue = Mock()
    msgs = Mock()
    msg = Mock()

    queue.poll.return_value = msgs

    msg = namedtuple("msg", "value")
    message_json = '{"time": 0.1, "code": 200, "exists": true}'\
        .encode('utf-8')

    msgs.items.return_value = [(0, [msg(value=message_json)])]

    consumer = Consumer(db, queue)

    # when
    result = consumer.job()

    # then
    assert result is True
    db.insert.assert_called_once()
    db.commit.assert_called_once()
    queue.commit.assert_called_once()
