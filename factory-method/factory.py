from french_localizer import FrenchLocalizer
from english_localizer import EnglishLocalizer
from spanish_localizer import SpanishLocalizer


def factory(language = "English"):
    localizers = {
        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer
    }
    return localizers[language]()


if __name__ == "__main__":

    f = factory("French")
    e = factory("English")
    s = factory("Spanish")

    message = ["car", "bike", "cycle"]

    for msg in message:
        print("\n" + f.localize(msg))
        print(e.localize(msg))
        print(s.localize(msg))
