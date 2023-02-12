from factory.namer import Namer


class FirstFirst(Namer):
    def __init__(self, name_string):
        super().__init__()
        i = name_string.find(" ")
        if i > 0:
            names = name_string.split()
            self.first = names[0]
            self.last = names[1]
        else:
            self.last = name_string
