# Задача 1: Управление банковским счетом
# Реализуйте класс BankAccount, который представляет банковский счет.
# Класс должен содержать атрибуты balance (баланс) и методы deposit (положить деньги на счет)
# и withdraw (снять деньги со счета). Создайте собственный класс исключения InsufficientFundsError,
# который будет возбуждаться при попытке снятия суммы, превышающей текущий баланс.

class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, money):
        if money < 0:
            raise ValueError("Сумма для пополнения должна быть больше 0")
        self.balance += money
        print(f'Cчет успешно пополнен на сумму {money}\nТекущий баланс - {self.balance}')

    def withdraw(self, money):
        if money < 0:
            raise ValueError("Сумма для снятия должна быть больше 0")

        if self.balance < money:
            raise ValueError("Недостаточно средств на счёте")

        self.balance -= money
        print(f'Снятие средств на сумму {money} успешно выполнено\nТекущий баланс - {self.balance}')

try:
    account = BankAccount(1000)
    account.deposit(500)
    account.withdraw(-200) #вызывается иключение
    account.withdraw(1500)
except InsufficientFundsError as error:
    print(f"Ошибка: {error}")
except ValueError as error:
    print(f"Ошибка: {error}")