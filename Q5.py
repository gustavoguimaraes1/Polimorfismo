from enum import Enum


class History[T]:

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("A capacidade deve ser positiva")

        self.__capacity = capacity
        self.__items: list[T] = []

    def add(self, item: T):
        self.__items.append(item)

        if len(self.__items) > self.__capacity:
            self.__items.pop(0)

    def latest(self) -> T:
        if len(self.__items) == 0:
            raise IndexError("Histórico vazio")

        return self.__items[-1]

    def items(self) -> tuple[T, ...]:
        return tuple(self.__items)

    def __len__(self) -> int:
        return len(self.__items)


class TemperatureMonitor:

    def __init__(self, window: int = 5):
        self.__history = History[float](window)

    def record(self, celsius: float):
        self.__history.add(celsius)

    def average(self) -> float:
        if len(self.__history) == 0:
            raise ValueError("Nenhuma leitura registrada")

        readings = self.__history.items()
        return sum(readings) / len(readings)


class TransactionKind(Enum):
    DEPOSIT = 1
    WITHDRAW = -1


class Transaction:

    def __init__(self, kind: TransactionKind, amount: float):
        if amount <= 0:
            raise ValueError("O valor deve ser positivo")

        self.__kind = kind
        self.__amount = amount

    def get_kind(self) -> TransactionKind:
        return self.__kind

    def get_amount(self) -> float:
        return self.__amount

    def signed_amount(self) -> float:
        return self.__amount * self.__kind.value

    def __str__(self) -> str:
        return f"{self.signed_amount():+.2f}"


class Statement:

    def __init__(self, size: int = 5):
        self.__history = History[Transaction](size)

    def record(self, transaction: Transaction):
        self.__history.add(transaction)

    def recent(self) -> tuple[Transaction, ...]:
        return self.__history.items()

    def net_total(self) -> float:
        total = 0

        for transaction in self.__history.items():
            total += transaction.signed_amount()

        return total

    def __str__(self) -> str:
        transactions = self.__history.items()

        if len(transactions) == 0:
            return "Nenhuma transação"

        lines = []

        for transaction in transactions:
            lines.append(f"{transaction!s:>20}")

        lines.append("-" * 20)
        lines.append(f"{self.net_total():>20.2f}")

        return "\n".join(lines)