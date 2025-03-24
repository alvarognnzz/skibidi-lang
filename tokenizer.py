from tokens import *

def tokenize(line):
    tokens = []
    chars = list(line)
    i = 0
    
    while i < len(chars):
        char = chars[i]
        
        if char == '"':
            tokens.append(TOKEN_DOUBLE_QUOTE)
            i += 1
            string_content = ""
            
            while i < len(chars) and chars[i] != '"':
                string_content += chars[i]
                i += 1
                
            if i < len(chars):
                tokens.append(f'{TOKEN_STRING}:{string_content}')
                tokens.append(TOKEN_DOUBLE_QUOTE)
            else:
                for c in string_content:
                    if c.isdigit():
                        tokens.append(f'{TOKEN_INT}:{c}')
                    else:
                        tokens.append(f'{TOKEN_CHAR}:{c}')
            
            i += 1
            continue
            
        elif char == "'":
            tokens.append(TOKEN_SINGLE_QUOTE)
            i += 1
            string_content = ""
            
            while i < len(chars) and chars[i] != "'":
                string_content += chars[i]
                i += 1
                
            if i < len(chars):
                tokens.append(f'{TOKEN_STRING}:{string_content}')
                tokens.append(TOKEN_SINGLE_QUOTE)
            else:
                for c in string_content:
                    if c.isdigit():
                        tokens.append(f'{TOKEN_INT}:{c}')
                    else:
                        tokens.append(f'{TOKEN_CHAR}:{c}')
            
            i += 1
            continue
        
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
        elif char == '=':
            tokens.append(TOKEN_EQUAL)
        elif char == ' ':
            tokens.append(TOKEN_SPACE)
        elif char == '.':
            tokens.append(TOKEN_DOT)
        else:
            tokens.append(f'{TOKEN_CHAR}:{char}')
            
        i += 1

    return tokens

def advanced_tokenize(tokens):
    parsed = []
    
    tokens.append(TOKEN_SPACE)
    
    i = 0
    current_word = []
    
    in_string = False
    string_content = ""
    
    while i < len(tokens):
        current_token = tokens[i]
        
        if current_token == TOKEN_DOUBLE_QUOTE or current_token == TOKEN_SINGLE_QUOTE:
            if current_word and not in_string:
                process_word(current_word, parsed)
                current_word = []
            
            if not in_string:
                in_string = True
                quote_type = current_token
                parsed.append(current_token)
                i += 1
                
                if i < len(tokens) and tokens[i].startswith(f"{TOKEN_STRING}:"):
                    parsed.append(tokens[i])
                    i += 1
                    
                    if i < len(tokens) and tokens[i] == quote_type:
                        parsed.append(tokens[i])
                        in_string = False
                        i += 1
                
                continue
            else:
                parsed.append(current_token)
                in_string = False
                i += 1
                continue
        
        if not in_string and current_token in [TOKEN_PLUS, TOKEN_MINUS, TOKEN_MUL, TOKEN_DIV, 
                                              TOKEN_LPAREN, TOKEN_RPAREN, TOKEN_EQUAL]:
            if current_word:
                process_word(current_word, parsed)
                current_word = []
            
            if current_token == TOKEN_EQUAL and i+1 < len(tokens) and tokens[i+1] == TOKEN_EQUAL:
                parsed.append(TOKEN_DOUBLE_EQUAL)
                i += 2
                continue
            
            parsed.append(current_token)
            i += 1
            continue
            
        elif not in_string and current_token == TOKEN_SPACE:
            if current_word:
                process_word(current_word, parsed)
                current_word = []
            i += 1
            continue
            
        else:
            if in_string:
                parsed.append(current_token)
            else:
                current_word.append(current_token)
            i += 1
    
    return parsed

def process_word(word, parsed):
    float_value = identify_float(word.copy())
    if float_value:
        parsed.append(f'{TOKEN_FLOAT}:{float_value}')
        return
    
    int_value = join_ints(word)
    if int_value:
        parsed.append(f'{TOKEN_INT}:{int_value}')
        return
    
    string_value = identify_string(word.copy())
    if string_value:
        parsed.append(f'{TOKEN_STRING}:{string_value}')
        return
    
    parsed.extend(word)

def join_double_equal(tokens):
    is_double_equal = True

    if len(tokens) == 2:
        for token in tokens:
            if not token == TOKEN_EQUAL:
                is_double_equal = False
    else:
        is_double_equal = False
    
    return '' if not is_double_equal else TOKEN_DOUBLE_EQUAL

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
    
    copied_tokens = tokens.copy()

    while copied_tokens and (copied_tokens[0].startswith("CHAR:") or copied_tokens[0].startswith("INT:")):
        if copied_tokens[0].startswith("CHAR:"):
            has_char = True
        string += copied_tokens.pop(0).split(":")[1]

    return string if has_char else ""