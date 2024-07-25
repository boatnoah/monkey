from monke_token.token import Token, TokenType, look_up_indent


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

    def next_token(self) -> Token:
        self.skip_whitespace()

        if self.ch == "=":
            if self.peek_char() == "=":
                ch = self.ch
                self.read_char()
                tok = Token(TokenType.EQ, ch + self.ch)
            else:
                tok = Token(TokenType.ASSIGN, self.ch)
        elif self.ch == "+":
            tok = Token(TokenType.PLUS, self.ch)
        elif self.ch == "-":
            tok = Token(TokenType.MINUS, self.ch)
        elif self.ch == "!":
            if self.peek_char() == "=":
                ch = self.ch
                self.read_char()
                tok = Token(TokenType.NOT_EQ, ch + self.ch)
            else:
                tok = Token(TokenType.BANG, self.ch)
        elif self.ch == "/":
            tok = Token(TokenType.SLASH, self.ch)
        elif self.ch == "*":
            tok = Token(TokenType.ASTERISK, self.ch)
        elif self.ch == "<":
            tok = Token(TokenType.LT, self.ch)
        elif self.ch == ">":
            tok = Token(TokenType.GT, self.ch)
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
            if self.ch.isalpha() or self.ch == "_":
                literal = self.read_identifier()
                token_type = look_up_indent(literal)
                tok = Token(token_type, literal)
                return tok
            elif self.ch.isdigit():
                tok = Token(TokenType.INT, self.read_number())
                return tok
            else:
                tok = Token(TokenType.ILLEGAL, self.ch)

        self.read_char()
        return tok

    def skip_whitespace(self):
        while self.ch in (" ", "\t", "\n", "\r"):
            self.read_char()

    def peek_char(self):
        if self.read_position >= len(self.input_data):
            return 0
        else:
            return self.input_data[self.read_position]

    def read_number(self) -> str:
        position = self.position
        while self.ch.isdigit():
            self.read_char()

        return self.input_data[position : self.position]

    def read_identifier(self) -> str:
        position = self.position
        while self.ch.isalpha():
            self.read_char()

        return self.input_data[position : self.position]
