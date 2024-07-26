import sys

from lexer.lexer import Lexer

PROMPT = ">> "


def start(input_stream=sys.stdin, output_stream=sys.stdout):

    running = True
    while running:
        output_stream.write(PROMPT)
        output_stream.flush()

        line = input_stream.readline()
        if not line:
            return

        l = Lexer(line)

        while running:
            tok = l.next_token()
            if tok.type == "EOF":
                break
            print(f"{tok}", file=output_stream)
