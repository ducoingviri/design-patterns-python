class FrenchLocalizer:

    def __init__(self):
        self.translations = {"car": "voiture", "bike": "bicyclette", "cycle": "cyclette"}

    def localize(self, msg):
        return self.translations.get(msg, msg)