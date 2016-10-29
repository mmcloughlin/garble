# garble

Randomize your data

## Install

```
python setup.py install
```

## CLI Usage

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
    "bool": false,
    "date": "2015-10-16T15:31:47+00:00",
    "float": 0.6366413658409333,
    "integer": 68,
    "list": [
        7,
        "E",
        8
    ],
    "none": null,
    "string": "cgmnaQwclPmM",
    "uuid": "c575987b-9f5c-4e5f-8606-f5b896fced1c"
}
```

## Library Usage

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