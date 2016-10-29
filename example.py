import garble
import pprint

data = {
        'string': 'Hello World!',
        'integer': 42,
        'float': 3.141592,
        'bool': True,
        'none': None,
        'list': [1, 'a', 3],
        'date': '2016-10-29T17:14:18+00:00',
        'uuid': '3ee0c4c1-e852-4735-b6c5-7fd7af6ee998',
        }
result = garble.garble(data)
pprint.pprint(result)
