import pyperclip as pc


class IOUtil:
    @staticmethod
    def to_clipboard(text: str) -> bool:
        pc.copy(text)
        return text == IOUtil.from_clipboard()

    @staticmethod
    def from_clipboard():
        return pc.paste()
