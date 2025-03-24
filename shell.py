from tokenizer import tokenize, advanced_tokenize
from parser import parse

if __name__ == '__main__':
    code = input("skibidi > ")
    tokens = tokenize(code)
    advanced_tokens = advanced_tokenize(tokens)
    parsed = parse(advanced_tokens)

    print(parsed)