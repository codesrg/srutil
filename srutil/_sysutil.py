from __future__ import annotations

import re
import uuid
import socket
import os.path
from pathlib import Path
from typing import AnyStr


class SysUtil:
    @staticmethod
    def home() -> str:
        home_dir = str(Path().home())
        return os.path.abspath(path=home_dir)

    @staticmethod
    def hostname() -> str:
        return socket.gethostname()

    @staticmethod
    def ipaddress() -> str:
        return socket.gethostbyname(SysUtil.hostname())

    @staticmethod
    def macaddress() -> str:
        return ':'.join(re.findall('..', '%012x' % uuid.getnode()))

    @staticmethod
    def executesyscmd(cmd: AnyStr | os.PathLike[AnyStr]):
        os.system(command=cmd)
