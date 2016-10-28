import string
import random


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


HANDLERS = [
        (type_predicate(dict), handle_dict),
        (type_predicate(list), handle_list),
        (type_predicate(str), handle_str),
        (type_predicate(int), handle_int),
        ]


def garble(x):
    for predicate, handler in HANDLERS:
        if predicate(x):
            return handler(x)
    return x
