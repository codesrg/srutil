# Srutil

[![PyPI](https://img.shields.io/pypi/v/srutil)](https://pypi.python.org/pypi/srutil)
[![Pypi - License](https://img.shields.io/github/license/codesrg/srutil)](https://github.com/codesrg/srutil/blob/main/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/srutil?color=red)](https://pypi.python.org/pypi/srutil)

Common Utils.

## Installation

`pip install -U srutil`

## Usage

Few usages of `srutil` package,

To get home directory
```python
from srutil import util
home_dir = util.home() 
```

###
To get random number between `6` and `30`
```python
from srutil import util
num = util.rand_num(6, 30)
```

###
To check if network is available
```python
from srutil import util
is_connected = util.isnetworkconnected()
```

###
To paste data from clipboard
```python
from srutil import util
data = util.from_clipboard()
```

###
To get current time in milliseconds
```python
from srutil import util
data = util.current_in_millis()
```


## Issues:

If you encounter any problems, please file an [issue](https://github.com/codesrg/srutil/issues) along with a detailed description.