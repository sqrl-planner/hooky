#!/usr/bin/env python3

#l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# l = [0, 1, 2]
#print(l[:-7:2])
#l[0:-3:2] = ['a', 'b', 'c', 'd']  # '['a', 'b', 'c', 'd', 'e', 'f', 'g']
#print(l)


class A:
    def __init__(self):
        self.a = 'a'


class B:
    def __init__(self):
        self.b = 'b'


class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        self.c = 'c'

z = C()

print(z.a, z.b, z.c)
