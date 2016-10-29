# garble

Randomize your data

## CLI

Here's `input.json`

```json
{
    "bool": true,
    "date": "2016-10-29T17:14:18+00:00",
    "float": 3.141592,
    "integer": 42,
    "list": [
        1,
        "a",
        3
    ],
    "none": null,
    "string": "Hello World!",
    "uuid": "3ee0c4c1-e852-4735-b6c5-7fd7af6ee998"
}
```

Run

```
$ garble < input.json | python -m json.tool
```

You get something like

```json
{
    "bool": true,
    "date": "2041-08-12T17:05:36+00:00",
    "float": 2.8047753673186078,
    "integer": 39,
    "list": [
        7,
        "z",
        4
    ],
    "none": null,
    "string": "TEoBECQaRjDT",
    "uuid": "02a97104-e323-47ee-a539-41dc8ff04b80"
}
```

## Usage

```python
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
```

Output:

```
{'bool': True,
 'date': '2035-01-23T01:02:32+00:00',
 'float': 5.241442620759742,
 'integer': 34,
 'list': [2, 'P', 9],
 'none': None,
 'string': 'EpcYNDIGPedu',
 'uuid': '481d2d6a-1784-4f6d-ad66-66345b531104'}
```