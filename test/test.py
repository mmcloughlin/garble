import random

import garble


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
        assert type(res) == int
        assert len(str(res)) == digits
