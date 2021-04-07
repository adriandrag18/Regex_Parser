from ERParser import ERParser
from ERVisitor import ERVisitor
from NFA import NFA
from ERtoNFA import concatenation, reunion, star


class ERVisitorToNFA(ERVisitor):

    def visitVariable(self, ctx: ERParser.VariableContext):
        return NFA(2, 0, {1}, {(0, str(ctx.VAR())): {1}})

    def visitSub_expr(self, ctx: ERParser.Sub_exprContext):
        expr = ctx.expr()
        if expr:
            return self.visit(expr)

    def visitAtom(self, ctx: ERParser.AtomContext):
        var = ctx.variable()
        sub_expr = ctx.sub_expr()

        if var:
            return self.visit(var)
        if sub_expr:
            return self.visit(sub_expr)

    def visitK_expr(self, ctx: ERParser.K_exprContext):
        return star(self.visit(ctx.atom()))

    def visitC_expr(self, ctx: ERParser.C_exprContext):
        atom = ctx.atom()
        k_expr = ctx.k_expr()

        if atom:
            return self.visit(atom)
        if k_expr:
            return self.visit(k_expr)
        if ctx.c_expr():
            c_expr1, c_expr2 = ctx.c_expr()
            return concatenation(self.visit(c_expr1), self.visit(c_expr2))

    def visitExpr(self, ctx: ERParser.ExprContext):
        expr = ctx.expr()
        c_expr = ctx.c_expr()

        if expr:
            return reunion(self.visit(c_expr), self.visit(expr))
        else:
            return self.visit(c_expr)
