from dataclasses import dataclass


@dataclass
class TokenType:
    ILLEGAL = "ILLEGAL"  # signifies token or character we don't know
    EOF = "EOF"  # Tells our parser that we can stop

    # Identifiers + literals
    IDENT = "IDENT"  # add, foobar, x, y etc...
    INT = "INT"  # 1324231b

    # Operators
    ASSIGN = "="
    PLUS = "+"
    MINUS = "-"
    BANG = "!"
    ASTERISK = "*"
    SLASH = "/"

    EQ = "=="
    NOT_EQ = "!="

    LT = "<"
    GT = ">"

    # Delimiters
    COMMA = ","
    SEMICOLON = ";"
    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"

    # Keywords
    FUNCTION = "FUNCTION"
    LET = "LET"
    TRUE = "TRUE"
    FALSE = "FALSE"
    IF = "IF"
    ELSE = "ELSE"
    RETURN = "RETURN"


@dataclass
class Token:
    type: str
    literal: str


keywords = {
    "fn": TokenType.FUNCTION,
    "let": TokenType.LET,
    "true": TokenType.TRUE,
    "false": TokenType.FALSE,
    "if": TokenType.IF,
    "else": TokenType.ELSE,
    "return": TokenType.RETURN,
}


def look_up_indent(indent): 
    return keywords.get(indent, TokenType.IDENT)
