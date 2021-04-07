import sys
from antlr4 import *
from ERLexer import ERLexer
from ERParser import ERParser
from ERVisitorToNFA import ERVisitorToNFA
from DFA import DFA

inp = FileStream(sys.argv[1])
lexer = ERLexer(inp)
stream = CommonTokenStream(lexer)
parser = ERParser(stream)
tree = parser.expr()
visitor = ERVisitorToNFA()
nfa = visitor.visit(tree)

with open(sys.argv[2], 'w') as file:
    print(nfa, file=file)

with open(sys.argv[3], 'w') as file:
    print(DFA.from_nfa(nfa), file=file)
