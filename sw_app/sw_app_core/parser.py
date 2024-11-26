from custom_token import INTEGER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, REGEX,EOF
import re
from lexer import Lexer
from context import Context
from arithmatic.addition_strategy import AdditionStrategy
from arithmatic.subtraction_strategy import SubtractionStrategy
from regex_folder.regex_class import RegexStrategy

class Parser:
    def __init__(self, lexer): 
        self.lexer = lexer
        self.current_token = None
        self.current_token = self.lexer.get_next_token() 
        self.context = None
   
    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        """Consume the current token and move to the next one."""
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        """factor : INTEGER | LPAREN expr RPAREN"""
        token = self.current_token
        if token.type == INTEGER:
            self.eat(INTEGER)
            return token.value
        elif token.type == LPAREN:
            self.eat(LPAREN)
            result = self.expr()
            self.eat(RPAREN)
            return result
        elif token.type == REGEX:
            return self.regex() 


    def term(self):
        """term : factor ((MUL | DIV) factor)*"""
        result = self.factor()

        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
                result = result * self.factor()
            elif token.type == DIV:
                self.eat(DIV)
                result = result / self.factor()

        return result

    def regex(self):
        """Parse and evaluate a REGEX operation."""
        regex_call = self.current_token.value  
        self.eat(REGEX)
        
        match = re.match(r"REGEX\('(.*?)','(.*?)'\)", regex_call)
        if not match:
            self.error()

        text, pattern = match.groups()
        self.context = Context(RegexStrategy())
        return self.context.executeStrategy(text, pattern)

    def expr(self):
        result = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
                self.context = Context(AdditionStrategy())
                result = self.context.executeStrategy(result,self.term())
            elif token.type == MINUS:
                self.eat(MINUS)
                self.context = Context(SubtractionStrategy())
                result = self.context.executeStrategy(result,self.term())


        return result
