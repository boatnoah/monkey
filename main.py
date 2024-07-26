import getpass
import sys

from repl import repl


def main():
    try:
        username = getpass.getuser()
    except Exception as e:
        print(f"Error getting current user: {e}")
        return

    print(f"Hello {username}! This is the Monkey programming language!")
    print("Feel free to type in commands")

    repl.start(input_stream=sys.stdin, output_stream=sys.stdout)


if __name__ == "__main__":
    main()
