from hooky import List, Dict

# the List and the Dict have four member: _before_add, _after_add, _before_del and _after_del, it's the hook

class NameList(List):
    def _before_add(self, key=None, item=None):
        if not isinstance(item, str):
            raise TypeError('item of NameList must be instance of str, not {}'.format(type(item)))


names = NameList()

names.append(b'Tom')


class Dict