class OperatorUtils():
    @classmethod
    def applyAssignmentOp(cls, left, op, right):
        if op == "=":
            return right
        elif op == "*=":
            return left * right
        elif op == "/=":
            return left / right
        elif op == "%=":
            return left % right
        elif op == "+=":
            return left + right
        elif op == "-=":
            return left - right
        elif op == "<<=":
            return left << right
        elif op == ">>=":
            return left >> right
        elif op == "^=":
            return left ^ right
        elif op == "|=":
            return left | right
        elif op == "&=":
            return left & right