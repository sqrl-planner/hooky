from collections import UserList, UserDict


class Hook(object):
    def _add_before_func(self, key=None, item=None):
        pass

    def _add_after_func(self, key=None, item=None):
        pass

    def _del_before_func(self, key=None):
        pass

    def _del_after_func(self, key=None):
        pass


class List(Hook, UserList):

    def __init__(self, initlist=None, hook_when_init=True):
        super().__init__(self)

        if initlist:
            if hook_when_init:
                self.extend(initlist)
            else:
                self.data.extend(initlist)

    def __setitem__(self, i, item):  # x[i] = item, del and add

        if isinstance(i, slice):
            if not hasattr(item, '__contains__'):
                raise TypeError('can only assign an iterable')

            start, stop, step = i.indices(len(self))

            ########################################################
            if step == 1:
                for one in range(stop - start):
                    del self[start]

                _i = start
                for one in item:
                    self.insert(_i, one)
                    _i += 1

            else:

                if step > 1:
                    slice_size = (stop - start) // step

                    if 0 < (stop - start) % step < step:
                        slice_size += 1
                else:
                    slice_size = (start - stop) // abs(step)

                    if 0 < (start - stop) % abs(step) < abs(step):
                        slice_size += 1

                slice_size = 0 if slice_size < 0 else slice_size
                if slice_size != len(item):
                    raise ValueError('attempt to assign sequence of size {} to extended slice of size {}'.format(
                        len(item), slice_size
                    ))

                _i = start
                for one in item:
                    self[_i] = one
                    _i += step

        else:
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


class Dict(Hook, UserDict):
    def __init__(self, initdict=None, hook_when_init=True):
        super().__init__(self)

        if initdict:
            if hook_when_init:
                self.update(initdict)
            else:
                self.data.update(initdict)

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
