
def f(*args, **kwargs):
    print(args)
    print(kwargs)


class A:
    def update(self, *args, **kwargs):

        print(args)
        print(kwargs)
        print()
        print()

        f(*args, **kwargs)

a = A()

a.update({'a': 1, 'b': 2}, c=3, d=4)
