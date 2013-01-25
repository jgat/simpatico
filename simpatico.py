#!/usr/bin/env python

from tokenizer import TokenReader as _TokenReader
from rules import get_rules as _get_rules

def check(filename):
    """Evaluate the style of a given file. Return a list of violations.

    check(str) -> list<Violation>

    Raises IOError on invalid filename.
    """
    rule_list = _get_rules()
    reader = _TokenReader(filename)
    errors = []

    # Check the code for violations
    for r in rule_list:
        reader.reset()
        r.check(reader)
        errors.extend(r.report())
    return sum((r.report() for r in rule_list), [])

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+")
    args = parser.parse_args()

    for fname in args.files:
        for violation in check(fname):
            print violation.format()
