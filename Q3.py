from abc import ABC, abstractmethod


class Payment(ABC):

    def __init__(self, amount: float):
        if amount <= 0:
            raise ValueError("O valor deve ser positivo")

        self.__amount = amount

    def get_amount(self) -> float:
        return self.__amount

    @abstractmethod
    def total(self) -> float:
        pass


class Pix(Payment):

    DISCOUNT = 0.05

    def total(self) -> float:
        return self.get_amount() * (1 - self.DISCOUNT)


class CreditCard(Payment):

    INTEREST = 0.03
    MAX_INSTALLMENTS = 12

    def __init__(self, amount: float, installments: int = 1):
        super().__init__(amount)

        if installments < 1 or installments > self.MAX_INSTALLMENTS:
            raise ValueError("Parcelas devem estar entre 1 e 12")

        self.__installments = installments

    def get_installments(self) -> int:
        return self.__installments

    def total(self) -> float:
        if self.__installments == 1:
            return self.get_amount()

        return self.get_amount() * (1 + self.INTEREST)


class Boleto(Payment):

    FEE = 3.50

    def total(self) -> float:
        return self.get_amount() + self.FEE


class CashRegister:

    def __init__(self):
        self.__payments = []

    def add(self, payment: Payment):
        self.__payments.append(payment)

    def total(self) -> float:
        total = 0

        for payment in self.__payments:
            total += payment.total()

        return total
