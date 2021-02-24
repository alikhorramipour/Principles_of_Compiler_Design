from lexer import Lexer
from pparser import Parser

lexer = Lexer().build()
file = open('test.txt')
text_input = file.read()
file.close()
lexer.input(text_input)
# while True:
#     tok = lexer.token()
#     if not tok: break
#     print(tok)
parser = Parser()
parser.build().parse(text_input, lexer, False)