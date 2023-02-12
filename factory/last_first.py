from factory.namer import Namer


class LastFirst(Namer):
    def __init__(self, name_string):
        super().__init__()
        i = name_string.find(",")
        if i > 0:
            names = name_string.split(",")
            self.last = names[0]
            self.first = names[1]
        else:
            self.last = name_string
