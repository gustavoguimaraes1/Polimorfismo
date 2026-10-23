from abc import ABC, abstractmethod


class Expr(ABC):

    @abstractmethod
    def solve(self):
        pass


class Operand(Expr):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Var(Operand):

    def __init__(self, name, value):
        super().__init__(value)
        self.name = name

    def solve(self):
        return self.value

    def __str__(self):
        return self.name


class Number(Operand):

    def __init__(self, value):
        super().__init__(value)

    def solve(self):
        return self.value


class Operation(Expr):

    def __init__(self, operator):
        self.operator = operator


class BinaryOperation(Operation):

    def __init__(self, operator, expr1, expr2):
        super().__init__(operator)

        self.expr1 = expr1
        self.expr2 = expr2

    def __str__(self):
        return f"({self.expr1}{self.operator}{self.expr2})"


class Sum(BinaryOperation):

    def __init__(self, expr1, expr2):
        super().__init__("+", expr1, expr2)

    def solve(self):
        return self.expr1.solve() + self.expr2.solve()


class Mul(BinaryOperation):

    def __init__(self, expr1, expr2):
        super().__init__("*", expr1, expr2)

    def solve(self):
        return self.expr1.solve() * self.expr2.solve()