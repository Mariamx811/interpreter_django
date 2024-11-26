from lexer import Lexer
from parser import Parser

class Interpreter:
    def __init__(self, text):
        self.text = text

    def interpret(self):
        lexer = Lexer(self.text)
        parser = Parser(lexer)
        return parser.expr()
