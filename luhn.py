# Credit Card Validator
# By Wallis

from binlist import BIN


def luhn(number):
    str_to_int = [int(x) for x in number]
    print(str_to_int)
    doubled = []
    str_to_int[::2] = [x * 2 for x in str_to_int[::2]]
    for x in str_to_int:
        x = sum(int(i) for i in str(x))
        doubled.append(x)
    summary = sum(doubled)
    if summary % 10 == 0:
        print('Valid')
    else:
        print('Not valid')


while True:
    try:
        card_number = str(input('Please enter credit card number: '))
        card_number = [i for a, i in enumerate(card_number) if i != ' ']
        luhn(card_number)
        print(BIN(card_number[0:3]).lookup())
    except ValueError:
        print('error')
        continue

