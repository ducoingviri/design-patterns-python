class SpanishLocalizer:

    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta", "cycle": "ciclo"}

    def localize(self, msg):
        return self.translations.get(msg, msg)
