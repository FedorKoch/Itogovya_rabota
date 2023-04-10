import text_fields

def main_menu() -> int:
    print('-------------')
    print(text_fields.main_menu)
    length_menu = len(text_fields.main_menu.split('\n')) - 1
    while True:
        choice = input('Выберите пукнт меню: ')
        if choice.isdigit() and 0 < int(choice) <= length_menu:
            return int(choice)
        else:
            print('Нужно вводить число из меню')

def show_message(message: str):
    print('-'*len(message))
    print(message)
    print('-'*len(message))