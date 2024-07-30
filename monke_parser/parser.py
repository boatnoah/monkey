from lexer.lexer import Lexer
from monke_ast.monke_ast import Program
from monke_token.token import Token


class Parser:
    def __init__(self, l: Lexer):
        self.l = l
        self.cur_token = None
        self.peek_token = None

        # Read two tokens, so cur_token and peek_token are both set
        self.next_token()
        self.next_token()

    def next_token(self):
        self.cur_token = self.peek_token
        self.peek_token = self.l.next_token()

    def parse_program(self) -> Program:
        return None


def new(lexer: Lexer) -> Parser:
    return Parser(lexer)
