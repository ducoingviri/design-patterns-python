from abc import ABCMeta, abstractmethod


class IPrototype(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def clone():
        return


class MyClass(IPrototype):

    def __init__(self, field):
        self.field = field

    def clone(self):
        return type(self)(
            self.field
        )

    def __str__(self):
        return f"{id(self)}\tfield={self.field}\ttype={type(self.field)}"


OBJECT1 = MyClass([1, 2, 3, 4])
print(f"OBJECT1 {OBJECT1}")

OBJECT2 = OBJECT1.clone()

OBJECT2.field[1] = 101

print(f"OBJECT2 {OBJECT2}")
print(f"OBJECT1 {OBJECT1}")
