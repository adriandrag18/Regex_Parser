# Generated from ER.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write("$\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\3\2\6\2\21\n\2\r\2\16\2\22\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\6\6\6\34\n\6\r\6\16\6\35\3\6\3\6\3\7\5\7#\n\7\2\2\b\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\3\2\4\4\2\13\f\"\"\4\2C\\c|\2")
        buf.write("%\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\3\20\3\2\2\2\5\24\3\2\2\2\7\26\3")
        buf.write("\2\2\2\t\30\3\2\2\2\13\33\3\2\2\2\r\"\3\2\2\2\17\21\7")
        buf.write(",\2\2\20\17\3\2\2\2\21\22\3\2\2\2\22\20\3\2\2\2\22\23")
        buf.write("\3\2\2\2\23\4\3\2\2\2\24\25\7~\2\2\25\6\3\2\2\2\26\27")
        buf.write("\7*\2\2\27\b\3\2\2\2\30\31\7+\2\2\31\n\3\2\2\2\32\34\t")
        buf.write("\2\2\2\33\32\3\2\2\2\34\35\3\2\2\2\35\33\3\2\2\2\35\36")
        buf.write("\3\2\2\2\36\37\3\2\2\2\37 \b\6\2\2 \f\3\2\2\2!#\t\3\2")
        buf.write("\2\"!\3\2\2\2#\16\3\2\2\2\6\2\22\35\"\3\b\2\2")
        return buf.getvalue()


class ERLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    KLEENE = 1
    REUNION = 2
    OPEN = 3
    CLOSED = 4
    WHITESPACE = 5
    VAR = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'|'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "KLEENE", "REUNION", "OPEN", "CLOSED", "WHITESPACE", "VAR" ]

    ruleNames = [ "KLEENE", "REUNION", "OPEN", "CLOSED", "WHITESPACE", "VAR" ]

    grammarFileName = "ER.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


