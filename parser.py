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

def join_ints(tokens):
    return "".join(token.split(":")[1] for token in tokens if token.startswith("INT:"))

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

    while tokens and (tokens[0].startswith("CHAR:") or tokens[0].startswith("INT:")):
        string += tokens.pop(0).split(":")[1]

    return string