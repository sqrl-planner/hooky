from collections import UserList, UserDict


class Hook:
    def add_before(self, key=None, item=None, obj=None):
        pass

    def add_after(self, key=None, item=None, obj=None):
        pass

    def del_before(self, key=None, item=None, obj=None):
        pass

    def del_after(self, key=None, item=None, obj=None):
        pass


class List(UserList):

    def __init__(self, initlist=None, hook=None, hook_when_init=True):
        self._hooks = []
        if hook:
            self._hooks.append(hook)

        super().__init__()

        if initlist:
            if hook_when_init:
                self.data.extend(initlist)
            else:
                self.extend(initlist)

    def __setitem__(self, i, item):  # x[i] = item, del and add
        del self[i]
        self.insert(i, item)

    # all del action should be here
    def __delitem__(self, i):  # del x[i], del
        [hook.del_before(key=i, obj=self) for hook in self._hooks]

        del self.data[i]

        [hook.add_after(key=i, obj=self) for hook in self._hooks]

    def append(self, item):  # add
        self.insert(len(self), item)

    # all add action should be here
    def insert(self, i, item):
        [hook.add_before(key=i, item=item, obj=self) for hook in self._hooks]

        self.data.insert(i, item)

        [hook.add_after(key=i, item=item, obj=self) for hook in self._hooks]

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


class Dict(UserDict):

    def __init__(self, initdict=None, hook=None, hook_when_init=True):
        self._hooks = []
        if hook:
            self._hooks.append(hook)

        initdict = initdict or {}

        super().__init__()

        if initdict:
            if hook_when_init:
                self.data.update(initdict)
            else:
                self.update(initdict)

    # all set action should be here
    def __setitem__(self, key, item):

        [hook.add_before(key=key, item=item, obj=self) for hook in self._hooks]

        self.data[key] = item

        [hook.add_after(key=key, item=item, obj=self) for hook in self._hooks]

    # all del action should be here
    def __delitem__(self, key):
        [hook.del_before(key=key, obj=self) for hook in self._hooks]

        del self.data[key]

        [hook.del_after(key=key, obj=self) for hook in self._hooks]
