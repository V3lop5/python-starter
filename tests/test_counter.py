from pytest import fixture

from counter import Counter


@fixture
def basic_counter():
    """
    Instance of the counter
    """
    return Counter(42)


def test_increment(basic_counter):
    basic_counter.add()
    assert basic_counter.counter == 43


def test_increment_two(basic_counter):
    basic_counter.add(increment=2)
    assert basic_counter.counter == 44


def test_reset(basic_counter):
    basic_counter.reset()
    assert basic_counter.counter == 42
