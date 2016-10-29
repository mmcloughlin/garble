import string
import random
import re
import uuid
import datetime
import types

import iso8601
import pytz


def type_predicate(type_):
    """
    type_predicate builds a function that tests if its argument has the given
    type.
    """
    return lambda x: type(x) == type_


def handle_dict(x):
    """
    handle_dict replaces a dictionary by recursively calling garble on all its
    values.
    """
    return {k: garble(v) for k, v in x.items()}


def handle_list(x):
    """
    handle_list replaces a list by recursively calling garble on all its
    entries.
    """
    return [garble(v) for v in x]


def random_string(n, alphabet=string.letters):
    """
    random_string generates a random string of length n consisting of
    characters from the given alphabet.
    """
    characters = [random.choice(alphabet) for _ in range(n)]
    return ''.join(characters)


def handle_str(x):
    """
    handle_str returns a random string of the same length as x.
    """
    return random_string(len(x))


def handle_int(x):
    """
    handle_int returns a random integer with the same number of digits as x.
    """
    digits = len(str(x))
    return random.randrange(10**(digits-1), 10**digits)


def handle_float(x):
    """
    handle_float returns a random float between 0 and 2x.
    """
    return x * random.uniform(0, 2)


def handle_bool(x):
    """
    handle_bool returns a random boolean.
    """
    return random.choice([False, True])


def handle_none(x):
    """
    handle_none returns None.
    """
    return None


UUID4_REGEX = re.compile('^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$')

def is_uuid4(x):
    """
    is_uuid4 returns True if x is a uuid4 string.
    """
    if type(x) not in [str, unicode]:
        return False
    return bool(UUID4_REGEX.match(x))


def handle_uuid4(x):
    """
    handle_uuid4 returns a random uuid4.
    """
    return str(uuid.uuid4())


def is_date(x):
    """
    is_date returns True if x is a string containing an ISO 8601 date.
    """
    if type(x) not in [str, unicode]:
        return False
    try:
        iso8601.parse_date(x)
    except:
        return False
    return True


def handle_date(x):
    """
    handle_date returns a random date in ISO 8601 format.
    """
    epoch = random.getrandbits(32)
    date = datetime.datetime.fromtimestamp(epoch, pytz.utc)
    return date.isoformat()


HANDLERS = [
        (type_predicate(dict), handle_dict),
        (type_predicate(list), handle_list),
        (is_uuid4, handle_uuid4),
        (is_date, handle_date),
        (type_predicate(str), handle_str),
        (type_predicate(unicode), handle_str),
        (type_predicate(long), handle_int),
        (type_predicate(int), handle_int),
        (type_predicate(bool), handle_bool),
        (type_predicate(float), handle_float),
        (type_predicate(types.NoneType), handle_none),
        ]


def garble(x):
    """
    garble returns randomized data with the same schema as x.
    """
    for predicate, handler in HANDLERS:
        if predicate(x):
            return handler(x)
    raise Exception('unhandled value')
