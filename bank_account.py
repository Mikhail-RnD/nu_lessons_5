account_balance = 0
purchase_history = []
# тут без глобальных переменных похоже никак, иначе при втоорм заходе не покажет баланс и список покупок
def my_banking():
    global account_balance
    global purchase_history


    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. баланс счета')
    print('5. выход')

    choice = input('Выберите пункт меню: ')

    while choice != '5':

        if choice == '1':
            account_balance += int(input('Введите сумму для пополнения: '))
        elif choice == '2':
            purchase = int(input('Введите сумму покупки: '))
            if purchase <= account_balance:
                purchase_history.append((input('Введите название покупки: '), purchase))
                balance -= purchase
        elif choice == '3':
            print(purchase_history)
        elif choice == '4':
            print(f'Баланс счета = {account_balance}')
        elif choice == '5':
            return
        else:
            print('Неверный пункт меню')

        choice = input('Выберите пункт меню: ')