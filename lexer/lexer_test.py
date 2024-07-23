# lexer/lexer_test.py

import unittest

from lexer import Lexer
from monke_token.token import TokenType


class TestTokenMethods(unittest.TestCase):
    def test_next_token(self):
        test_input = "=+(){},;"
        tests = [
            (TokenType.ASSIGN, "="),
            (TokenType.PLUS, "+"),
            (TokenType.LPAREN, "("),
            (TokenType.RPAREN, ")"),
            (TokenType.LBRACE, "{"),
            (TokenType.RBRACE, "}"),
            (TokenType.COMMA, ","),
            (TokenType.SEMICOLON, ";"),
            (TokenType.EOF, ""),
        ]

        l = Lexer(test_input)
        for i, (expected_type, expected_literal) in enumerate(tests):
            token = l.next_token()
            self.assertEqual(
                token.type,
                expected_type,
                f"tests[{i}] - tokentype wrong. expected={expected_type}, got={token.type}",
            )
            self.assertEqual(
                token.literal,
                expected_literal,
                f"tests[{i}] - literal wrong. expected='{expected_literal}', got='{token.literal}'",
            )

        print("hello")


if __name__ == "__main__":
    unittest.main()
