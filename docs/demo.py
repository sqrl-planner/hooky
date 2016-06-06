from hooky import List, Dict


# demo for List
class NameList(List):
    def _before_add(self, key=None, item=None):
        if not isinstance(item, str):
            raise TypeError('item of NameList must be instance of str, not {}'.format(item.__class__.__name__))

names = NameList(['John', 'Alissa'])

# Will raise TypeError here
names.append(b'Tom')