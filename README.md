# pyhandlers

-----

**Table of Contents**

* [Installation](#installation)
* [Sample usage](#sample-usage)
* [License](#license)

## Installation

pyhandlers is distributed on [PyPI](https://pypi.org) as a universal
wheel and is available on Linux/macOS and Windows and supports
Python 3.6+.

```bash
$ pip install pyhandlers
```

## Sample usage

```python
from pyhandlers import error_handler

#a simple example of error_handler usage

def char_fixer(string): 
    if "O" in string:
        return string.replace("O", "0")
    else:
        return string

date_error_handler = error_handler((ValueError, ), default=char_fixer)

from dateutil import parser

@date_error_handler
def date_parser(date):
    return parser.parse(date)

```

## License

pyhandlers is distributed under the terms of the
[MIT License](https://choosealicense.com/licenses/mit).
