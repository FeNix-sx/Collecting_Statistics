from datetime import datetime
from colorama import init, Fore, Style


init(autoreset=True)

class ColorInput:
    def __init__(self, patern: list=None) -> None:
        self.__patern = [
            item.strftime('%d.%m.%Y') for item in self.__check_value(patern)
        ]

    @staticmethod
    def __check_value(patern):
        if patern and isinstance(patern, list):
            return patern
        else:
            raise ValueError(Fore.LIGHTRED_EX + Style.BRIGHT + "Не задан список допустимых значений")

    def cinput_date(self, message):
        while True:
            try:
                input_data = input(Fore.CYAN + Style.BRIGHT + message)
                input_data = datetime.strptime(input_data, '%d.%m.%Y')

                if datetime.strptime(self.__patern[0], '%d.%m.%Y') <= \
                        input_data \
                        <= datetime.strptime(self.__patern[1], '%d.%m.%Y'):
                    break
                else:
                    print(Fore.LIGHTRED_EX + Style.BRIGHT + "Дата за пределами диапазона. Повторите попытку.")

            except Exception as ex:
                print(Fore.LIGHTRED_EX + Style.BRIGHT + "Ошибка! Формат ввода 00.00.0000\nПовторите попытку.")

        return input_data

    def cinput_int(self, message):
        while True:
            try:
                index = input(Fore.CYAN + Style.BRIGHT + message)

                if int(index) in list(range(1, 4)):
                    break
                else:
                    print(Fore.LIGHTRED_EX + Style.BRIGHT + "Неверное значение. Повторите попытку.")

            except Exception as ex:
                print(Fore.LIGHTRED_EX + Style.BRIGHT + "Ошибка! Формат ввода 00.00.0000\nПовторите попытку.")

        return int(index)


class ColorPrint:

    def __print(self, color_style, *args, **kwargs):
        message = [color_style + arg for arg in args]
        print(*message, **kwargs)

    def print_error(self, *args, **kwargs):
        self.__print(Fore.LIGHTRED_EX + Style.BRIGHT, *args, **kwargs)

    def print_info(self, *args, **kwargs):
        self.__print(Fore.GREEN + Style.BRIGHT, *args, **kwargs)

    def print_warning(self, *args, **kwargs):
        self.__print(Fore.CYAN + Style.BRIGHT, *args, **kwargs)

    def print_yellow(self, *args, **kwargs):
        self.__print(Fore.YELLOW + Style.BRIGHT, *args, **kwargs)