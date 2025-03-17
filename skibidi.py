TOKEN_INT = "INT"
TOKEN_FLOAT = "FLOAT"
TOKEN_CHAR = "CHAR"
TOKEN_PLUS = "PLUS"
TOKEN_MINUS = "MINUS"
TOKEN_MUL = "MUL"
TOKEN_DIV = "DIV"
TOKEN_LPAREN = "LPAREN"
TOKEN_RPAREN = "RPAREN"

# Tokenized chains are a way to translate characters into tokens the parser can recognize.
def tokenize(line):
    tokens = []
    
    chars = list(line)

    for char in chars:
        if char.isdigit():
            tokens.append(f'{TOKEN_INT}:{char}')
        
        elif char == '(':
            tokens.append(f'{TOKEN_LPAREN}')
        
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

        else:
            tokens.append(f'{TOKEN_CHAR}:{char}')
    
    return tokens