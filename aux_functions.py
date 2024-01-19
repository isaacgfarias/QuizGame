import os


def valid_input(text: str, options: list):
    while True:
        output = input(text).lower()
        for o in map(str, options):
            if not o.isdigit():
                o = o.lower()
            if o == output:
                return output
        print('\nInvalid option. Try', ' or '.join(
            o for o in map(str, options)) + '.\n')
        

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')