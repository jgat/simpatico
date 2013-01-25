from collections import namedtuple
from abc import ABCMeta, abstractmethod

ViolationBase = namedtuple("ViolationBase",
        ["filename", "line", "category", "description"])

class Violation(ViolationBase):
    _PRINT_FORMAT = "{0.filename}:{0.line}: [{0.category}] {0.description}"
    def format(self):
        return self._PRINT_FORMAT.format(self)

class RuleChecker(object):
    """An abstract class for checking and reporting on rules."""
    __metaclass__ = ABCMeta
    _CATEGORY = NotImplemented

    def __init__(self):
        self._errors = []

    def _error(self, file_line, message):
        """Report an error on the given line number (counting lines from 1)"""
        fname, lnum = file_line
        v = Violation(fname, lnum, self._CATEGORY, message)
        self._errors.append(v)

    @abstractmethod
    def check(self, reader):
        raise NotImplementedError

    def report(self):
        return sorted(self._errors)

