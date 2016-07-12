from hooky import List, Dict


# List
class NameList(List):
    def _before_add(self, key=None, item=None):
        if not isinstance(item, str):
            print('Type: {} is not well'.format(type(item)))
            # of cause you may want raise here
        else:
            print('fine')

# two fine
names = NameList(['Sue', 'Alissa'])

# fine
names.append('ben')

# not well
names.append(b'Tom')


# Dict
class Files(Dict):
    def _before_add(self, key=None, item=None):
        if not isinstance(key, str):
            raise TypeError
        if '/' in key:
            raise KeyError('invalid filename')

files = Files()

# fine
files['1.xml'] = '<test></test>'

# raise keyError:
files['tes/t.txt'] = b'text'
