from monke_token.token import Token, TokenType


class Lexer:
    def __init__(self, input_data):
        self.input_data: str = input_data
        self.position: int = 0
        self.read_position: int = 0
        self.ch: str = ""
        self.read_char()

    def read_char(self):
        if self.read_position >= len(self.input_data):
            self.ch = "\0"
        else:
            self.ch = self.input_data[self.read_position]

        self.position = self.read_position
        self.read_position += 1

    def next_token(self):
        self.skip_whitespace()
        if self.ch == "=":
            tok = Token(TokenType.ASSIGN, self.ch)
        elif self.ch == "+":
            tok = Token(TokenType.PLUS, self.ch)
        elif self.ch == "(":
            tok = Token(TokenType.LPAREN, self.ch)
        elif self.ch == ")":
            tok = Token(TokenType.RPAREN, self.ch)
        elif self.ch == "{":
            tok = Token(TokenType.LBRACE, self.ch)
        elif self.ch == "}":
            tok = Token(TokenType.RBRACE, self.ch)
        elif self.ch == ",":
            tok = Token(TokenType.COMMA, self.ch)
        elif self.ch == ";":
            tok = Token(TokenType.SEMICOLON, self.ch)
        elif self.ch == "\0":
            tok = Token(TokenType.EOF, "")
        else:
            tok = Token(TokenType.ILLEGAL, self.ch)

        self.read_char()
        return tok

    def skip_whitespace(self):
        while self.ch in (" ", "\t", "\n", "\r"):
            self.read_char()
