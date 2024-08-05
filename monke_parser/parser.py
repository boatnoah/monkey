from lexer.lexer import Lexer
from monke_ast.monke_ast import Identifier, LetStatement, Program
from monke_token import token
from monke_token.token import Token, TokenType


class Parser:
    def __init__(self, l: Lexer):
        self.l = l
        self.errors = []
        # Read two tokens, so cur_token and peek_token are both set
        self.cur_token = None
        self.peek_token = None
        self.next_token()
        self.next_token()

    def next_token(self):
        self.cur_token = self.peek_token
        self.peek_token = self.l.next_token()

    def cur_token_is(self, t):
        return self.cur_token and self.cur_token.type == t

    def peek_token_is(self, t):
        return self.peek_token and self.peek_token.type == t

    def expect_peek(self, t):
        if self.peek_token_is(t):
            self.next_token()
            return True
        else:
            self.peek_errors(t)
            return False

    def parse_let_statements(self):
        stmt = LetStatement(self.cur_token)

        if not self.expect_peek(TokenType.IDENT):
            return None

        stmt.name = Identifier(self.cur_token, self.cur_token.literal)

        if not self.expect_peek(TokenType.ASSIGN):
            return None

        while not self.cur_token_is(TokenType.SEMICOLON):
            self.next_token()

        return stmt

    def parse_statement(self):
        if self.cur_token and self.cur_token.type == TokenType.LET:
            return self.parse_let_statements()
        else:
            return None

    def parse_program(self) -> Program:
        program = Program()

        while self.cur_token.type != "EOF":
            stmt = self.parse_statement()
            if stmt:
                program.statements.append(stmt)

            self.next_token()

        return program

    def get_errors(self):
        return self.errors

    def peek_errors(self, t):
        msg = f"expected next token to be {t}, got {self.peek_token.type}"
        self.errors.append(msg)


def new(lexer: Lexer) -> Parser:
    return Parser(lexer)
