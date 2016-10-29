import string
import random
import re
import uuid
import datetime

import iso8601
import pytz


def type_predicate(type_):
    return lambda x: type(x) == type_


def handle_dict(x):
    return {k: garble(v) for k, v in x.items()}


def handle_list(x):
    return [garble(v) for v in x]


def random_string(n, alphabet=string.letters):
    characters = [random.choice(alphabet) for _ in range(n)]
    return ''.join(characters)


def handle_str(x):
    return random_string(len(x))


def handle_int(x):
    digits = len(str(x))
    return random.randrange(10**(digits-1), 10**digits)


def handle_float(x):
    return x * random.uniform(0, 2)


def handle_bool(x):
    return random.choice([False, True])


UUID4_REGEX = re.compile('^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$')

def is_uuid4(x):
    if type(x) not in [str, unicode]:
        return False
    return bool(UUID4_REGEX.match(x))


def handle_uuid4(x):
    return str(uuid.uuid4())


def is_date(x):
    if type(x) not in [str, unicode]:
        return False
    try:
        iso8601.parse_date(x)
    except:
        return False
    return True


def handle_date(x):
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
        ]


def garble(x):
    for predicate, handler in HANDLERS:
        if predicate(x):
            return handler(x)
    raise Exception('unhandled value')
