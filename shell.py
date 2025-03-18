from tokenizer import tokenize
from parser import parse

if __name__ == '__main__':
    code = input("skibidi > ")
    tokens = tokenize(code)
    parsed = parse(tokens)
    
    print(parsed)