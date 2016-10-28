import random

import garble
import garble.handlers


def test_str():
    x = 'Hello World!'
    res = garble.garble(x)
    assert type(res) == str
    assert len(res) == len(x)


def test_int():
    x = 0
    for digits in range(1, 20):
        x = 10 * x + random.randrange(10)
        res = garble.garble(x)
        assert type(res) in [int, long]
        assert len(str(res)) == digits


def test_uuid4():
    x = '09dac315-8e9e-45ef-ab2c-c7309d0be083'
    res = garble.garble(x)
    assert garble.handlers.is_uuid4(res)
