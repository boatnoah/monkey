from abc import ABC, abstractmethod
from monke_token.token import Token

class Node(ABC):
    @abstractmethod
    def token_literal(self) -> str:
        pass

class Statement(Node):
    @abstractmethod
    def statement_node(self):
        pass

class Expression(Node):
    @abstractmethod
    def expression_node(self):
        pass


class Program:
    def __init__(self):
        self.statements = []

    def token_literal(self) -> str:
        if len(self.statements) > 0:
            return self.statements[0].token_literal()
        else:
            return ""

class LetStatement(Statement):
    def __init__(self, token, name, value):
        self.token = token  # the token.LET token
        self.name = name    # Identifier
        self.value = value  # Expression

    def statement_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal

class Identifier(Expression):
    def __init__(self, token, value):
        self.token = token  # the token.IDENT token
        self.value = value  # string

    def expression_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal
