from factory.namer_factory import NamerFactory


class Builder:

    def compute(self):
        name = ""
        while name != 'quit':
            name = input("Enter name: ")
            namer_factory = NamerFactory(name)
            namer = namer_factory.get_namer()
            print(namer.first, namer.last)


def main():
    builder = Builder()
    builder.compute()


if __name__ == "__main__":
    main()
