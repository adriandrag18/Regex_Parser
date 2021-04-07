# Generated from ER.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
        buf.write("/\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\3\2\3\2\5\2\24\n\2\3\3\3\3\3\3\5\3\31\n\3\3\3")
        buf.write("\3\3\7\3\35\n\3\f\3\16\3 \13\3\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\6\3\6\5\6+\n\6\3\7\3\7\3\7\2\3\4\b\2\4\6\b\n\f")
        buf.write("\2\2\2,\2\23\3\2\2\2\4\30\3\2\2\2\6!\3\2\2\2\b$\3\2\2")
        buf.write("\2\n*\3\2\2\2\f,\3\2\2\2\16\17\5\4\3\2\17\20\7\4\2\2\20")
        buf.write("\21\5\2\2\2\21\24\3\2\2\2\22\24\5\4\3\2\23\16\3\2\2\2")
        buf.write("\23\22\3\2\2\2\24\3\3\2\2\2\25\26\b\3\1\2\26\31\5\6\4")
        buf.write("\2\27\31\5\n\6\2\30\25\3\2\2\2\30\27\3\2\2\2\31\36\3\2")
        buf.write("\2\2\32\33\f\5\2\2\33\35\5\4\3\6\34\32\3\2\2\2\35 \3\2")
        buf.write("\2\2\36\34\3\2\2\2\36\37\3\2\2\2\37\5\3\2\2\2 \36\3\2")
        buf.write("\2\2!\"\5\n\6\2\"#\7\3\2\2#\7\3\2\2\2$%\7\5\2\2%&\5\2")
        buf.write("\2\2&\'\7\6\2\2\'\t\3\2\2\2(+\5\f\7\2)+\5\b\5\2*(\3\2")
        buf.write("\2\2*)\3\2\2\2+\13\3\2\2\2,-\7\b\2\2-\r\3\2\2\2\6\23\30")
        buf.write("\36*")
        return buf.getvalue()


class ERParser ( Parser ):

    grammarFileName = "ER.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'|'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "KLEENE", "REUNION", "OPEN", "CLOSED", 
                      "WHITESPACE", "VAR" ]

    RULE_expr = 0
    RULE_c_expr = 1
    RULE_k_expr = 2
    RULE_sub_expr = 3
    RULE_atom = 4
    RULE_variable = 5

    ruleNames =  [ "expr", "c_expr", "k_expr", "sub_expr", "atom", "variable" ]

    EOF = Token.EOF
    KLEENE=1
    REUNION=2
    OPEN=3
    CLOSED=4
    WHITESPACE=5
    VAR=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def c_expr(self):
            return self.getTypedRuleContext(ERParser.C_exprContext,0)


        def REUNION(self):
            return self.getToken(ERParser.REUNION, 0)

        def expr(self):
            return self.getTypedRuleContext(ERParser.ExprContext,0)


        def getRuleIndex(self):
            return ERParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ERParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        try:
            self.state = 17
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 12
                self.c_expr(0)
                self.state = 13
                self.match(ERParser.REUNION)
                self.state = 14
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.c_expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class C_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def k_expr(self):
            return self.getTypedRuleContext(ERParser.K_exprContext,0)


        def atom(self):
            return self.getTypedRuleContext(ERParser.AtomContext,0)


        def c_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ERParser.C_exprContext)
            else:
                return self.getTypedRuleContext(ERParser.C_exprContext,i)


        def getRuleIndex(self):
            return ERParser.RULE_c_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitC_expr" ):
                return visitor.visitC_expr(self)
            else:
                return visitor.visitChildren(self)



    def c_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ERParser.C_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_c_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 20
                self.k_expr()
                pass

            elif la_ == 2:
                self.state = 21
                self.atom()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 28
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ERParser.C_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_c_expr)
                    self.state = 24
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 25
                    self.c_expr(4) 
                self.state = 30
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class K_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(ERParser.AtomContext,0)


        def KLEENE(self):
            return self.getToken(ERParser.KLEENE, 0)

        def getRuleIndex(self):
            return ERParser.RULE_k_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitK_expr" ):
                return visitor.visitK_expr(self)
            else:
                return visitor.visitChildren(self)




    def k_expr(self):

        localctx = ERParser.K_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_k_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.atom()
            self.state = 32
            self.match(ERParser.KLEENE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Sub_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self):
            return self.getToken(ERParser.OPEN, 0)

        def expr(self):
            return self.getTypedRuleContext(ERParser.ExprContext,0)


        def CLOSED(self):
            return self.getToken(ERParser.CLOSED, 0)

        def getRuleIndex(self):
            return ERParser.RULE_sub_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub_expr" ):
                return visitor.visitSub_expr(self)
            else:
                return visitor.visitChildren(self)




    def sub_expr(self):

        localctx = ERParser.Sub_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_sub_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(ERParser.OPEN)
            self.state = 35
            self.expr()
            self.state = 36
            self.match(ERParser.CLOSED)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(ERParser.VariableContext,0)


        def sub_expr(self):
            return self.getTypedRuleContext(ERParser.Sub_exprContext,0)


        def getRuleIndex(self):
            return ERParser.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = ERParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_atom)
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ERParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.variable()
                pass
            elif token in [ERParser.OPEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.sub_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ERParser.VAR, 0)

        def getRuleIndex(self):
            return ERParser.RULE_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = ERParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(ERParser.VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.c_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def c_expr_sempred(self, localctx:C_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




