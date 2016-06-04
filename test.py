#!/usr/bin/env python3

from hooky import List, Dict


class Count:
    def __init__(self):
        self.ab_count = 0
        self.af_count = 0

        self.db_count = 0
        self.df_count = 0

    def _add_before_func(self, key=None, item=None):
        self.ab_count += 1

    def _add_after_func(self, key=None, item=None):
        self.af_count += 1

    def _del_before_func(self, key=None):
        self.db_count += 1

    def _del_after_func(self, key=None):
        self.df_count += 1


class CountList(Count, List):
    def __init__(self, *args, **kwargs):
        Count.__init__(self)
        List.__init__(self, *args, **kwargs)


class CountDict(Count, Dict):
    def __init__(self, *args, **kwargs):
        Count.__init__(self)
        Dict.__init__(self, *args, **kwargs)


def test_list_add():
    add_count = 0
    l = CountList()

    l.append(99)
    add_count += 1

    l.extend(['a', 'hello', None, {None: 's'}])
    add_count += 4

    l.insert(2, 3.14)
    add_count += 1

    l += [3, 'a', 'hello', 'world']
    add_count += 4

    assert add_count == l.ab_count == l.af_count


def test_list_del():
    del_count = 0
    l = CountList([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

    l.pop()
    del_count += 1

    l.remove(5)
    del_count += 1

    assert del_count == l.db_count == l.df_count


def test_list_add_del():
    add_count = 0
    del_count = 0

    l = CountList([0, 1, 2])
    add_count += 3

    l[2] = None
    del_count += 1
    add_count += 1

    assert add_count == l.ab_count == l.af_count

    assert del_count == l.db_count == l.df_count


def test_dict_add():
    add_count = 0

    d = CountDict()
    d['hello'] = 'world'
    d[42] = None


def test_dict_del():
    pass


def test_dict_add_del():
    pass
