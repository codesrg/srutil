import re


class StringBuilder:
    def __init__(self):
        self.__to_return = None

    def append(self, string: str, separator: str = "") -> "StringBuilder":
        itr = []
        if self.__to_return:
            itr.append(self.__to_return)
        itr.append(string)
        if string:
            self.__to_return = separator.join(itr)
        return self

    def tostring(self) -> str:
        return str(self.__to_return) if self.__to_return else ''


class StringUtil:
    @staticmethod
    def replacesubstringswithastring(*pattern, string: str, repl: str = "") -> str:
        """
        replace substrings `*pattern` with `string`
        Example: replacesubstringswithastring('a', 'b', string='abcd', repl='x') -> 'xxcd'
        """
        new_string = re.sub(StringUtil.stringbuilder(*pattern, separator='|'), repl, string)
        return new_string

    @staticmethod
    def stringbuilder(*args: str, separator: str = "") -> str:
        """
        append tuple of strings using separator
        example: stringbuilder("a", "b", "c", separator=".") -> 'a.b.c'
        """
        sb = StringBuilder()
        for arg in args:
            sb.append(arg, separator=separator)
        return sb.tostring()
