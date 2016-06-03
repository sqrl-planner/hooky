from collections import UserList, UserDict


class Hook:
    def _add_before_func(self, key=None, item=None):
        pass

    def _add_after_func(self, key=None, item=None):
        pass

    def _del_before_func(self, key=None):
        pass

    def _del_after_func(self, key=None):
        pass


class List(UserList, Hook):

    def __init__(self, initlist=None, hook_when_init=True):
        super().__init__()

        if initlist:
            if hook_when_init:
                self.data.extend(initlist)
            else:
                self.extend(initlist)

    def __setitem__(self, i, item):  # x[i] = item, del and add

        # if isinstance(i, slice):

        # print('start:{}, stop:{}, step:{}'.format(i.start, i.stop, i.step))
        # print(i.indices())

        del self[i]
        self.insert(i, item)

    # all del action should be here
    def __delitem__(self, i):  # del x[i], del
        self._del_before_func(key=i)
        del self.data[i]
        self._del_after_func(key=i)

    def append(self, item):  # add
        self.insert(len(self), item)

    # all add action should be here
    def insert(self, i, item):
        self._add_before_func(key=i, item=item)
        self.data.insert(i, item)
        self._add_after_func(key=i, item=item)

    def pop(self, i=-1):  # del
        x = self[i]
        del self[i]
        return x

    def remove(self, item):  # del
        i = self.index(item)
        del self[i]

    def clear(self):  # del
        for i in range(len(self)):
            self.pop()

    def extend(self, other):  # add
        for item in other:
            self.append(item)

    def __iadd__(self, other):  # x += y, add
        self.extend(other)
        return self

    def __imul__(self, n):  # x *= y, add
        old_data = self.copy()
        for x in range(n):
            self.extend(old_data)
        return self


class Dict(UserDict, Hook):
    def __init__(self, initdict=None, hook_when_init=True):
        initdict = initdict or {}
        super().__init__()

        if initdict:
            if hook_when_init:
                self.data.update(initdict)
            else:
                self.update(initdict)

    # all set action should be here
    def __setitem__(self, key, item):
        if key in self.keys():
            del self[key]

        self._add_before_func(key=key, item=item)
        self.data[key] = item
        self._add_after_func(key=key, item=item)

    # all del action should be here
    def __delitem__(self, key):
        self._del_before_func(key=key)
        del self.data[key]
        self._del_after_func(key=key)
