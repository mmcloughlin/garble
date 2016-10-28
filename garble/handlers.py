import string
import random
import re
import uuid


def type_predicate(type_):
    return lambda x: type(x) == type_


def handle_dict(x):
    print 'handle_dict'
    return {k: garble(v) for k, v in x.items()}


def handle_list(x):
    print 'handle_list'
    return [garble(v) for v in x]


def random_string(n, alphabet=string.letters):
    characters = [random.choice(alphabet) for _ in range(n)]
    return ''.join(characters)


def handle_str(x):
    print 'handle_str:', x
    return random_string(len(x))


def handle_int(x):
    print 'handle_int:', x
    digits = len(str(x))
    return random.randrange(10**(digits-1), 10**digits)


def handle_bool(x):
    return random.choice([False, True])


UUID4_REGEX = re.compile('^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$')

def is_uuid4(x):
    if type(x) not in [str, unicode]:
        return False
    return bool(UUID4_REGEX.match(x))


def handle_uuid4(x):
    print 'handle_uuid:', x
    return str(uuid.uuid4())


HANDLERS = [
        (type_predicate(dict), handle_dict),
        (type_predicate(list), handle_list),
        (is_uuid4, handle_uuid4),
        (type_predicate(str), handle_str),
        (type_predicate(unicode), handle_str),
        (type_predicate(long), handle_int),
        (type_predicate(int), handle_int),
        (type_predicate(bool), handle_bool),
        ]


def garble(x):
    for predicate, handler in HANDLERS:
        if predicate(x):
            return handler(x)
    return None
