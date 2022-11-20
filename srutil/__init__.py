"""Common utils."""

from .util import Util
from ._stringutil import StringBuilder

util = Util()
sb = StringBuilder()


__author__ = "srg"
__version__ = "1.0.1"

__all__ = [
    'util',
    'sb'
]
