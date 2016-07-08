from hooky import Dict


class MyDict(Dict):
    def _before_del(self, key=None):
        print('before_del, key:', key)

    def _after_del(self, key=None):
        print('after_del, key:', key)


d = MyDict({'a': 1, 'b': 2, 'c': 3, None: 4})

del d[None]

del d['a']

k, v = d.popitem()

print(d)
