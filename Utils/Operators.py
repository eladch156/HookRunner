class OperatorUtils():
    @classmethod
    def apply_assignment_op(cls, left, op, right):
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
