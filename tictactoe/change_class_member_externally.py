class Judger:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def change(self):
        self.p1.epsilon = 0.001
        self.p2.epsilon = 0.001

    def print(self):
        self.p1.print_epsilon()
        self.p2.print_epsilon()


class Player:
    def __init__(self, epsilon=0.01):
        self.epsilon = 0.01

    def print_epsilon(self):
        print(self.epsilon)


p1 = Player()
p2 = Player()

J = Judger(p1, p2)
J.print()
p1.epsilon = 0.02
J.print()


# 인수가 integer인 경우 차이점을 주목
class Judger_int:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def change(self):
        self.p1 = 0.02
        self.p2 = 0.02

    def print(self):
        print(self.p1, self.p2)

    #


i = 1
j = 2
#
J2 = Judger_int(i, j)
J2.print()
i = 3
J2.print()


class Parent:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


class Child(Parent):
    def __init__(self, c1, c2, **kwargs):
        self.c1 = c1
        self.c2 = c2
        super().__init__(**kwargs)
        self.c3 = "this is child's c3"


# child = Child(c1="this is child's c1", c2="this is child's c2", p1="this is parent's p1", p2="this is parent's p2")

child = Child("this is child's c1", "this is child's c2", p2="this is parent's p2", p1="this is parent's p1")

print(child.p1)
print(child.p2)
print(child.c1)
print(child.c2)
print(child.c3)

l = list([1, 2, 3, 4, 5])
s = set([1, 1, 2, 2, 3])
print(l)
print(s)
print(len(s))

import matplotlib.pyplot as plt
import numpy as np

print(np.random.randint(5))

a = ['a', 'b', 'c', 'd', 'e', 'f']
selection = []
for i in range(10000):
    selection.append(a[np.random.randint(len(a))])
plt.hist(selection, 6)
plt.show()
