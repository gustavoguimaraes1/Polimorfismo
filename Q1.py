from functools import total_ordering


@total_ordering
class Fraction:

    def __init__(self, num: int, den: int = 1):
        self.num = num
        self.den = den

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, value):
        self.__num = value

    @property
    def den(self):
        return self.__den

    @den.setter
    def den(self, value):
        if value == 0:
            raise ZeroDivisionError("O denominador não pode ser zero.")

        # Se o denominador for negativo,
        # transfere o sinal para o numerador.
        if value < 0:
            self.__num *= -1
            value *= -1

        self.__den = value

    def __add__(self, other: "Fraction") -> "Fraction":
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den

        return Fraction(num, den)

    def __sub__(self, other: "Fraction") -> "Fraction":
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den

        return Fraction(num, den)

    def __mul__(self, other: "Fraction") -> "Fraction":
        num = self.num * other.num
        den = self.den * other.den

        return Fraction(num, den)

    def __truediv__(self, other: "Fraction") -> "Fraction":
        if other.num == 0:
            raise ZeroDivisionError("Não é possível dividir por uma fração igual a zero.")

        num = self.num * other.den
        den = self.den * other.num

        return Fraction(num, den)

    def to_float(self) -> float:
        return self.num / self.den

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.num * other.den == other.num * self.den

        if isinstance(other, int):
            return self.num == other * self.den

        if isinstance(other, float):
            return self.to_float() == other

        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.num * other.den < other.num * self.den

        if isinstance(other, int):
            return self.num < other * self.den

        if isinstance(other, float):
            return self.to_float() < other

        return NotImplemented

    @staticmethod
    def gcd(a: int, b: int) -> int:
        a = abs(a)
        b = abs(b)

        while b != 0:
            a, b = b, a % b

        return a

    @staticmethod
    def lcm(a: int, b: int) -> int:
        if a == 0 or b == 0:
            return 0

        return abs(a * b) // Fraction.gcd(a, b)

    def is_common_factor(self, factor: int) -> bool:
        if factor == 0:
            return False

        return self.num % factor == 0 and self.den % factor == 0

    def reduce(self, common_factor: int):
        if not self.is_common_factor(common_factor):
            raise ValueError(
                f"{common_factor} não é fator comum de {self}"
            )

        self.num //= common_factor
        self.den //= common_factor

    def simplify(self):
        common_factor = self.gcd(self.num, self.den)
        self.reduce(common_factor)

    def __str__(self) -> str:
        return f"{self.num}/{self.den}"