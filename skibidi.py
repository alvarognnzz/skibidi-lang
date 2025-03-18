TOKEN_INT = "INT"
TOKEN_FLOAT = "FLOAT"
TOKEN_CHAR = "CHAR"
TOKEN_PLUS = "PLUS"
TOKEN_MINUS = "MINUS"
TOKEN_MUL = "MUL"
TOKEN_DIV = "DIV"
TOKEN_LPAREN = "LPAREN"
TOKEN_RPAREN = "RPAREN"
TOKEN_COLON = "COLON"
TOKEN_DOUBLE_QUOTE = "DOUBLE_QUOTE"
TOKEN_SINGLE_QUOTE = "SINGLE_QUOTE"
TOKEN_EQUAL = "EQUAL"
TOKEN_SPACE = 'SPACE'
TOKEN_DOT = 'DOT'

# Special tokens that are identified thanks to the parser
TOKEN_STRING = "STRING"
TOKEN_FLOAT = "FLOAT"

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

def parse(tokens):
    parsed = []

    words = []
    temp = []

    for token in tokens:
        if token == 'SPACE':
            if temp:
                words.append(temp)
                temp = []
        else:
            temp.append(token)

    if temp:
        words.append(temp)

    for word in words:
        identified_float = identify_float(word)
        if identified_float != "":
            parsed.append(f'{TOKEN_FLOAT}:{identified_float}')

        string = identify_string(word)
        if string != "":
            parsed.append(f'{TOKEN_STRING}:{string}')
        else:
            if identified_float == '':
                parsed.append(word)
    
    return parsed

def identify_string(tokens):
    string = ""
    
    while tokens and tokens[0].startswith("CHAR:"):
        string += tokens.pop(0).split(":")[1]
    
    return string

def identify_float(tokens):
    if (len(tokens) >= 3 and tokens[0].startswith("INT:") 
            and tokens[1] == "DOT" and tokens[2].startswith("INT:")):
        int_part = tokens.pop(0).split(":")[1]
        tokens.pop(0)
        decimal_part = tokens.pop(0).split(":")[1]
        return f"{int_part}.{decimal_part}"

    return ''

if __name__ == '__main__':
    tokens = tokenize("Test line 23 3.1 =- 6 /2*6: =")
    print(parse(tokens))
