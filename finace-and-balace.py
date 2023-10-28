# Общий баланс денег на счету

balance_money = 0.00


def add_money(refill):
    global balance_money
    if refill >= 0:
        balance_money += refill
        return balance_money
    else:
        print("НЕ ВЕРНАЯ СУММА")
        return False


while True:
    refill_money = (input("Пополнить счет: "))

    try:
        refill_money = float(refill_money)
        new_balance = add_money(refill_money)
        print(f"На вашем балансе: {new_balance}")
    except ValueError:
        print("Ошибка")


