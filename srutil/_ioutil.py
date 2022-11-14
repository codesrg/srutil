from __future__ import annotations
import getpass as gp
import pyperclip as pc
from typing import TextIO


class IOUtil:
    @staticmethod
    def to_clipboard(text: str) -> bool:
        pc.copy(text)
        return text == IOUtil.from_clipboard()

    @staticmethod
    def from_clipboard():
        return pc.paste()

    @staticmethod
    def getpass(prompt='Password: ', stream: TextIO | None = None):
        """Prompt for a password, with echo turned off."""
        return gp.getpass(prompt=prompt, stream=stream)
