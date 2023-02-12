from factory.last_first import LastFirst
from factory.first_first import FirstFirst


class NamerFactory:

    def __init__(self, name_string):
        self.name = name_string

    def get_namer(self):
        i = self.name.find(",")
        if i > 0:
            return LastFirst(self.name)
        else:
            return FirstFirst(self.name)
