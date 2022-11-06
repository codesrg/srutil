from __future__ import annotations

from ._ioutil import IOUtil
from ._sysutil import SysUtil
from ._kutil import KnowledgeUtil
from ._numberutil import NumberUtil
from ._stringutil import StringUtil
from ._networkutil import NetworkUtil
from ._datetimeutil import DateTimeUtil


class CoreUtil:
    @staticmethod
    def isobjtype(instance: object, cls: type) -> bool:
        """
        True if `obj` isinstanceof `target_type`
        similar to isinstance()
        """
        return type(instance) is cls

    @staticmethod
    def getinstanceof(obj: object, target, default=None, manage_exception: bool = False):
        """
        Cast `obj` to `target` type
        :raises TypeError
        """
        to_return = default
        if not isinstance(target, type):
            target = type(target)
        try:
            to_return = target(obj)
        except TypeError as e:
            if manage_exception is False:
                raise e
        return to_return


class Util(CoreUtil, IOUtil, SysUtil, StringUtil, NumberUtil, DateTimeUtil, NetworkUtil, KnowledgeUtil):
    pass
