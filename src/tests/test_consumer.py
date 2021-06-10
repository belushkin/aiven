from unittest.mock import Mock
from consumer import Consumer


def test_consumer_insert_when_it_receives_empty_dict():
    # given
    db = Mock()
    consumer = Consumer(db)

    # when
    result = consumer.insert({})

    # then
    assert result is False


def test_consumer_insert_when_it_receives_dict_without_time():
    # given
    db = Mock()
    consumer = Consumer(db)

    # when
    result = consumer.insert({'code': 200, 'exists': True})

    # then
    assert result is False


def test_consumer_insert_when_it_receives_dict_without_code():
    # given
    db = Mock()
    consumer = Consumer(db)

    # when
    result = consumer.insert({'time': 0.1, 'exists': True})

    # then
    assert result is False


def test_consumer_insert_when_it_receives_dict_without_exists():
    # given
    db = Mock()
    consumer = Consumer(db)

    # when
    result = consumer.insert({'time': 0.1, 'code': 200})

    # then
    assert result is False


def test_consumer_insert_when_it_receives_not_dict():
    # given
    db = Mock()
    consumer = Consumer(db)

    # when
    result = consumer.insert(False)

    # then
    assert result is False


def test_consumer_insert_when_it_receives_correct_dict():
    # given
    db = Mock()
    pg = Mock()
    db.getConn.return_value = pg
    consumer = Consumer(db)

    # when
    result = consumer.insert({'time': 0.1, 'code': 200, 'exists': True})

    # then
    assert result is True
    assert db.getConn.call_count == 2
    pg.commit.assert_called_once()
    pg.insert.assert_called_once()
