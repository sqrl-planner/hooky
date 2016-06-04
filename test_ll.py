#!/usr/bin/env python3

from hooky import List, Dict


def test_list_add():
    class ListAdd(List):
        def __init__(self):
            super().__init__(self)
            self.ab_count = 0
            self.af_count = 0

        def _add_before_func(self, key=None, item=None):
            self.ab_count += 1

        def _add_after_func(self, key=None, item=None):
            self.af_count += 1

    add_count = 0
    l = ListAdd()
    for attr, arg in (('append', 99), ('extend', ['a', 'c', 9, '27'])):
        getattr(l, attr)(arg)
        if isinstance(arg, list):
            add_count += len(arg)
        else:
            add_count += 1

        l.insert(0, 3.14)
        add_count += 1

        l += [3, 'a', 'hello', 'world']
        add_count += 4

    assert add_count == l.ab_count == l.af_count


def test_list_del():
    