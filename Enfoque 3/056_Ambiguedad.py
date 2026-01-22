
class AmbiguityExample:
    def __init__(self):
        self.sentences = []

    def add_sentence(self, sentence):
        self.sentences.append(sentence)

    def analyze(self):
        for sentence in self.sentences:
            print(f"Frase: {sentence}")
            print("Análisis de ambigüedad:")
            if "banco" in sentence:
                print(" - Puede referirse a una institución financiera o a un banco de río.")
            if "voló" in sentence:
                print(" - Puede referirse a un pájaro que voló o a alguien que lanzó algo.")
            print()

# Crear un analizador de ambigüedad
ambiguity_analyzer = AmbiguityExample()
ambiguity_analyzer.add_sentence("Fui al banco a retirar dinero.")
ambiguity_analyzer.add_sentence("El pájaro voló sobre el río.")
ambiguity_analyzer.add_sentence("El banco del río estaba lleno de peces.")

# Analizar las frases
ambiguity_analyzer.analyze()
