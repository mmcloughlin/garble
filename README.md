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
$ garble --input input.json --output output.json
```

You get something like

```json
{"none": null, "string": "bqwRTLYXhUdd", "float": 3.9680427329168895, "list": [8, "R", 4], "bool": false, "date": "2078-09-21T18:54:20+00:00", "integer": 55, "uuid": "37c2bf6d-af4b-400f-83e0-dc0355149902"}
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