
import re

class LexicalAnalyzer:
    def __init__(self):
        self.tokens = []

    def analyze(self, text):
        # Definir patrones para los tokens
        patterns = {
            "IDENTIFICADOR": r"\b[a-zA-Z_][a-zA-Z0-9_]*\b",
            "NÚMERO": r"\b\d+\b",
            "SÍMBOLO": r"[+*/-]",
            "PARÉNTESIS": r"[()]",
            "ESPACIO": r"\s+"
        }

        # Extraer tokens
        for token_type, pattern in patterns.items():
            matches = re.finditer(pattern, text)
            for match in matches:
                if token_type != "ESPACIO":  # Ignorar espacios
                    self.tokens.append((token_type, match.group()))

    def show_tokens(self):
        print("Tokens encontrados:")
        for token in self.tokens:
            print(f"{token[0]}: {token[1]}")

# Crear un analizador léxico

analyzer = LexicalAnalyzer()
sample_text = "x = 3 + 5 * (y - 2)"
analyzer.analyze(sample_text)


# Mostrar los tokens
analyzer.show_tokens()
