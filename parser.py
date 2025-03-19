from tokens import *

def parse(tokens):
    parsed = []

    words = []
    temp = []

    for token in tokens:
        if token == TOKEN_SPACE:
            if temp:
                words.append(temp)
                temp = []
        else:
            temp.append(token)

    if temp:
        words.append(temp)

    for word in words:
        joined_int = join_ints(word)
        if joined_int != '':
            parsed.append(f'{TOKEN_INT}:{joined_int}')

        identified_float = identify_float(word)
        if identified_float != "":
            parsed.append(f'{TOKEN_FLOAT}:{identified_float}')

        identified_string = identify_string(word)
        if identified_string != "":
            parsed.append(f'{TOKEN_STRING}:{identified_string}')
        else:
            if identified_float == '' and joined_int == '':
                parsed.append(word)

    return parsed

def join_double_equal(tokens):
    pass    

def join_ints(tokens):
    joined_int = ''
    
    is_int = True
    
    for token in tokens:
        if not token.startswith("INT:"):
            is_int = False
            break

    if is_int:
        for token in tokens:
            joined_int += token.split(':')[1]

    return joined_int

def identify_float(tokens):
    if len(tokens) >= 3 and tokens[0].startswith("INT:") and tokens[1] == TOKEN_DOT and tokens[2].startswith("INT:"):
        int_part = tokens.pop(0).split(":")[1]
        tokens.pop(0)

        decimal_part = tokens.pop(0).split(":")[1]
        while tokens and tokens[0].startswith("INT:"):
            decimal_part += tokens.pop(0).split(":")[1]

        return f"{int_part}.{decimal_part}"

    return ''

def identify_string(tokens):
    string = ""
    has_char = False

    while tokens and (tokens[0].startswith("CHAR:") or tokens[0].startswith("INT:")):
        if tokens[0].startswith("CHAR:"):
            has_char = True
        string += tokens.pop(0).split(":")[1]

    return string if has_char else ""
