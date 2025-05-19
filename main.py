from lss.lexer import lexer
from lss.parser import parser
from lss.executor import execute
import sys

if len(sys.argv) != 2:
    print("Usage: python main.py <scripts/file.lss>")
    sys.exit(1)

script = open(sys.argv[1], encoding='utf-8').read()
ast = parser.parse(script, lexer=lexer)
execute(ast)
print() # \n
