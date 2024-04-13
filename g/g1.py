import colorama
from colorama import Fore, Back, Style

'''Colorama - бібліотека для змінення тексту.

Colorama додає Fore (колір тексту), Back (фон тексту) і Style (стиль тексту)'''

print(Fore.RED + 'Hello World!')

'Щоб збросити налаштування використайте Style.RESET_ALL'

print(Style.RESET_ALL)
print(Back.RED + 'Hello World!')
print(Style.RESET_ALL)

'Інакше вийде:'

print(Fore.RED + 'Hello World!')
print(Back.GREEN + 'Hello World!')
print(Style.RESET_ALL)

'або'

print(Fore.BLUE)
print(Back.YELLOW + 'Hello World!')






