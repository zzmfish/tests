#!/usr/bin/python
#encoding=utf-8

#案例1
def iseven(n):
    return True if n == 0 else isodd(n - 1)

def isodd(n):
    return False if n == 0 else iseven(n - 1)

print(iseven(7))

#案例2
class Person:
    def set_name(self, name):
        self._name = name

    def name(self):
        return self._name

    def info(self):
        return {'name': self.name()}

person = Person()
person.set_name('Mike')
print person.info()
