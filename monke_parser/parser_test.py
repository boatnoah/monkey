import unittest

from lexer.lexer import Lexer
from monke_ast.monke_ast import LetStatement
from monke_parser.parser import Parser, new


class TestLetStatements(unittest.TestCase):
    def test_let_statements(self):
        input_data = """
        let x = 5;
        let y = 10;
        let 838383;
        """
        lexer = Lexer(input_data)
        parser = new(lexer)
        program = parser.parse_program()
        self.check_parser_errors(parser)
        self.assertIsNotNone(program, "parse_program() returned None")
        self.assertEqual(
            len(program.statements),
            3,
            f"program.statements does not contain 3 statements. got={len(program.statements)}",
        )
        expected_identifiers = ["x", "y", "foobar"]

        for i, expected_identifier in enumerate(expected_identifiers):
            stmt = program.statements[i]
            self.assertTrue(self.check_let_statement(stmt, expected_identifier))

    def check_let_statement(self, statement, name):
        self.assertEqual(
            statement.token_literal(),
            "let",
            f"statement.token_literal not 'let'. got={statement.token_literal()}",
        )

        self.assertIsInstance(
            statement,
            LetStatement,
            f"statement not LetStatement. got={type(statement)}",
        )

        self.assertEqual(
            statement.name.value,
            name,
            f"statement.name.value not '{name}'. got={statement.name.value}",
        )

        self.assertEqual(
            statement.name.token_literal(),
            name,
            f"statement.name not '{name}'. got={statement.name}",
        )

        return True

    def check_parser_errors(self, p: Parser):
        errors = p.get_errors()

        if not errors:
            return

        self.fail(
            f"parser has {len(errors)} errors:\n"
            + "\n".join(f"parser error: {msg}" for msg in errors)
        )


if __name__ == "__main__":
    unittest.main()
