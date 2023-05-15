# Напишите функцию, которая отображает пустой или заполненный квадрат из некоторого символа.
def print_square(side, symbol, filled):
    for i in range(side):
        for j in range(side):

           if filled or i == 0 or j == 0 or i == side - 1 or j == side - 1:

               print(symbol, end=' ')

           else:

               print(' ', end=' ')

        print()

print_square(6, '*', True)

print_square(6, '*', False)