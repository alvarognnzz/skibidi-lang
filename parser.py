from tokens import *

KEYWORD_ASSIGN_VARIABLE = "rizz"

def get_token(tokens, pos):
    return tokens[pos] if pos < len(tokens) else None

def get_token_value(token):
    return token.split(":")[1] if ":" in token else token

def parse_expression(tokens, pos):
    token = get_token(tokens, pos)
    
    # Handle numbers
    if token and (token.startswith(f"{TOKEN_INT}:") or token.startswith(f"{TOKEN_FLOAT}:")):
        value = get_token_value(token)
        return {"type": "Number", "value": value}, pos + 1
    
    # Handle string literals
    elif token == TOKEN_DOUBLE_QUOTE or token == TOKEN_SINGLE_QUOTE:
        quote = token
        pos += 1
        
        string_token = get_token(tokens, pos)
        if string_token and string_token.startswith(f"{TOKEN_STRING}:"):
            string_value = get_token_value(string_token)
            pos += 1
            
            if get_token(tokens, pos) == quote:
                pos += 1  # Consume closing quote
                return {"type": "String", "value": string_value}, pos
        
        return {"type": "String", "value": ""}, pos
    
    # Handle identifiers (variable names)
    elif token and (token.startswith(f"{TOKEN_CHAR}:") or token.startswith(f"{TOKEN_STRING}:")):
        name = get_token_value(token)
        pos += 1
        
        # Check for assignment
        if get_token(tokens, pos) == TOKEN_EQUAL:
            pos += 1  # Consume equal sign
            value, new_pos = parse_expression(tokens, pos)
            return {"type": "Assignment", "variable": name, "value": value}, new_pos
        
        # Just a variable reference
        return {"type": "Variable", "name": name}, pos
    
    # Handle operators
    elif token in [TOKEN_PLUS, TOKEN_MINUS, TOKEN_MUL, TOKEN_DIV]:
        return {"type": "Operator", "value": token}, pos + 1
    
    # Handle parentheses
    elif token == TOKEN_LPAREN or token == TOKEN_RPAREN:
        return {"type": "Parenthesis", "value": token}, pos + 1
    
    # Skip unknown tokens
    elif token:
        return {"type": "Unknown", "value": token}, pos + 1
    
    return {"type": "End"}, pos

def parse(tokens):
    results = []
    pos = 0
    
    while pos < len(tokens):
        expr, new_pos = parse_expression(tokens, pos)
        if expr:
            results.append(expr)
            pos = new_pos
        else:
            pos += 1  # Skip this token
    
    return results