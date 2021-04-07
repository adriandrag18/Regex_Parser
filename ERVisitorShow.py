from ERParser import ERParser
from ERVisitor import ERVisitor


class ERVisitorShow (ERVisitor):

    def visitVariable(self, ctx: ERParser.VariableContext):
        print(ctx.VAR())
        return self.visitChildren(ctx)
