INTEGER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, REGEX,EOF = (
    'Regex','INTEGER', 'PLUS', 'MINUS', 'MUL', 'DIV', '(', ')', 'EOF'
)
class Token:
    """Represents a single token."""
    def __init__(self, type, value):
        self.type = type  # Token type: INTEGER, PLUS, MINUS, or EOF
        self.value = value  # Token value: a number, '+', '-', or None

    def __str__(self):
        return f"Token({self.type}, {repr(self.value)})"

    def __repr__(self):
        return self.__str__()
