from custom_token import Token, INTEGER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, REGEX,EOF
import re

class Lexer:
    """
    Lexer - Responsible for breaking the input into tokens.
    """
    token_map = {
    '+': PLUS,
    '-': MINUS,
    '*': MUL,
    '/': DIV,
    '(': LPAREN,
    ')': RPAREN,
}

    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        """Move the position pointer and update `current_char`."""
        self.pos += 1
        if self.pos >= len(self.text):
            self.current_char = None  # End of input
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        """Return a multidigit integer."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)
    
    def match_regex(self):
        """Match and extract REGEX function call."""
        regex_pattern = r"REGEX\('(.*?)','(.*?)'\)"
        match = re.match(regex_pattern, self.text[self.pos:])
        if match:
            matched_text = match.group(0)
            self.pos += len(matched_text)
            self.current_char = None if self.pos >= len(self.text) else self.text[self.pos]
            return matched_text
        self.error()

    def get_next_token(self):
        """Tokenize the input string."""
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())
            
            if self.text[self.pos:].startswith('REGEX'):
                return Token(REGEX, self.match_regex())

            if self.current_char in self.token_map:
                type = self.token_map[self.current_char]
                char = self.current_char
                self.advance()
                return Token(type,char)
            
            if self.text[self.pos:].startswith('REGEX'):
                return Token(REGEX, self.match_regex())

           
            self.error()

        return Token(EOF, None)