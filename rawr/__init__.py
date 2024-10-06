from tokenizer import tokenize
from parser import parse
from runtime import execute_ast

def entry_point(argv):
    with open(argv[1], "r") as f:
        code = f.read()

    tokens = tokenize(code)
    ast = parse(tokens)
    execute_ast(ast)

    return 0

def target(*args):
    return entry_point

if __name__ == "__main__":
    from sys import argv
    entry_point(argv)