print("Введите номер кредитной карты")
card = input()


def card_hide(card):
    return '*' * len(card[:-4]) + card[-4:]