KEYWORD_ASSIGN_VARIABLE = "rizz"
ACTION_ASSIGN_VARIABLE = "ASSIGN"

def parse(tokens):
    is_assigning = False

    instruction = ""

    i = 0
    while tokens and i < len(tokens):
        if tokens[i].startswith('STRING:') and tokens[0].split(":")[1] == KEYWORD_ASSIGN_VARIABLE:
            instruction += ACTION_ASSIGN_VARIABLE + "("
            is_assigning = True
            i += 1

        if tokens[i].startswith('INT:'):
            instruction += tokens[i].split(':')[1]
            if is_assigning: instruction += ","
            
            break

    print(instruction)

def advance():
    pass