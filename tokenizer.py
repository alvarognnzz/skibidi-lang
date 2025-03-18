from tokens import *

def tokenize(line):
    tokens = []
    chars = list(line)

    for char in chars:
        if char.isdigit():
            tokens.append(f'{TOKEN_INT}:{char}')

        elif char == '(':
            tokens.append(TOKEN_LPAREN)

        elif char == ')':
            tokens.append(TOKEN_RPAREN)

        elif char == '+':
            tokens.append(TOKEN_PLUS)

        elif char == '-':
            tokens.append(TOKEN_MINUS)

        elif char == '*':
            tokens.append(TOKEN_MUL)

        elif char == '/':
            tokens.append(TOKEN_DIV)

        elif char == ':':
            tokens.append(TOKEN_COLON)

        elif char == '"':
            tokens.append(TOKEN_DOUBLE_QUOTE)

        elif char == "'":
            tokens.append(TOKEN_SINGLE_QUOTE)

        elif char == '=':
            tokens.append(TOKEN_EQUAL)

        elif char == ' ':
            tokens.append(TOKEN_SPACE)

        elif char == '.':
            tokens.append(TOKEN_DOT)

        else:
            tokens.append(f'{TOKEN_CHAR}:{char}')

    return tokens