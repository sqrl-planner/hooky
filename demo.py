from hooky import List, Dict


class NameList(List):
    def _before_add(self, key=None, item=None):
        if not isinstance(item, str):
            raise TypeError('item of NameList must be instance of str, not {}'.format(type(item)))


names = NameList(['John', 'Alissa'])

# Will raise
names.append(b'Tom')
