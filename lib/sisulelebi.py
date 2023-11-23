from colorama import Fore, Back, Style, init

init(autoreset=True)


def loading(current, max_value, bar_length=40):
    progress = current / max_value
    arrow = '▉' * int(round(bar_length * progress))
    spaces = ' ' * (bar_length - len(arrow))
    loading_bar = f'{Back.WHITE}{Fore.BLACK}[{Fore.GREEN}{arrow}{Style.RESET_ALL}{spaces}{Back.WHITE}{Fore.BLACK}]{Style.RESET_ALL} {current}/{max_value}'
    return loading_bar


def spinning_cursor():
    while True:
        for cursor in "|/-\\":
            yield cursor


spinner = spinning_cursor()
