# Generated from ER.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ERParser import ERParser
else:
    from ERParser import ERParser

# This class defines a complete generic visitor for a parse tree produced by ERParser.

class ERVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ERParser#expr.
    def visitExpr(self, ctx:ERParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ERParser#c_expr.
    def visitC_expr(self, ctx:ERParser.C_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ERParser#k_expr.
    def visitK_expr(self, ctx:ERParser.K_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ERParser#sub_expr.
    def visitSub_expr(self, ctx:ERParser.Sub_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ERParser#atom.
    def visitAtom(self, ctx:ERParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ERParser#variable.
    def visitVariable(self, ctx:ERParser.VariableContext):
        return self.visitChildren(ctx)



del ERParser