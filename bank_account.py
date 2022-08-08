account_balance = 0
purchase_history = []

def purchase(balance):
    purchase = int(input('Введите сумму покупки: '))
    if purchase < balance:
        purchase_history.append((input('Введите название покупки: '), purchase))
        balance -= purchase
    return balance

def my_banking():
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. баланс счета')
    print('5. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        account_balance += int(input('Введите сумму для пополнения: '))
    elif choice == '2':
        account_balance = purchase(account_balance)
    elif choice == '3':
        print(purchase_history)
    elif choice == '4':
        print(f'Баланс счета = {account_balance}')
    elif choice == '5':
        return
    else:
        print('Неверный пункт меню')