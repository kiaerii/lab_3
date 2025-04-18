#4
class BankAccount:
    def __init__(self, initial_balance=0): #создание счета и начальный баланс
        self._balance = initial_balance
        self._transactions = []  #список для хранения истории операций
    
    def deposit(self, amount): #Пополнение счета на указанную сумму
        if amount <= 0:
            raise ValueError('Сумма пополнения должна быть положительной')
        self._balance += amount #кол-во 
        self._transactions.append(f'Пополнение: +{amount}')
    
    def withdraw(self, amount): #Снятие средств со счета
        if amount <= 0: #кол-во денег 
            raise ValueError('Сумма снятия должна быть положительной')
        if amount > self._balance:
            raise ValueError('Недостаточно средств')
        self._balance -= amount
        self._transactions.append(f'Снятие: -{amount}')
    
    @property
    def balance(self): #Геттер для получения текущего баланса
        return self._balance
    
    def get_transactions(self): #Метод для получения истории операций
        return self._transactions.copy()


account = BankAccount(1000) #создаем банковский счет
account.deposit(500) #пополнение
print(f'Баланс после пополнения: {account.balance}')
account.withdraw(300) #снимаем средства
print(f'Баланс после снятия: {account.balance}')
try: #попытка снять больше, чем есть на счете
    account.withdraw(1500)
except ValueError as e:
    print(f'Ошибка: {e}')

print('История операций:', account.get_transactions()) #вывод истории операций
