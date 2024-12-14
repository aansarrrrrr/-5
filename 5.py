from colorama import init, Fore, Back, Style
init()  # Инициализация colorama

print(Fore.RED + "This is red text!" + Style.RESET_ALL)  # Красный текст
print(Back.GREEN + "This has a green background!" + Style.RESET_ALL)  # Зеленый фон
print(Style.BRIGHT + "This is bright text!" + Style.RESET_ALL)  # Яркий текст
