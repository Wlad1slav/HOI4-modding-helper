from PIL import Image
import os
from colorama import init, Fore


# directory = 'C:\Users\Natalia\Desktop\Wlad\Python\simulator_flags' #забавно, но не пашет

def formater():
    directory = input("Путь к папке флагов: ")

    try:
        files = os.listdir(directory) #arr
    except:
        print(f"{Fore.RED}Ошибка! Неправильно указан путь.\n")
        formater()

    try:
        images = filter(lambda x: x.endswith('.tga'), files) 

        for name in images:
            print('.', end='')
            try:
                flag = Image.open(f"{directory}\{name}")

                flag.thumbnail((41, 26))
                flag.save(f"{directory}\medium\{name}")

                flag.thumbnail((10, 7))
                flag.save(f"{directory}\small\{name}")
            except:
                print(f"{Fore.RED}Ошибка при открытии или форматировании {name}")
                try: errors+=1
                except: errors=1
        print()

    except:
        print(f"{Fore.RED}Ошибка при считывании файлов!\n")
        formater()
    
    print(f"{Fore.GREEN}Флаги успешно отформатированы!")
    try: print(f"{Fore.RED}Всего {errors} ошибок при форматировании!")
    except: print(f"{Fore.GREEN}Нет ошибок при форматировании.")

    print()
    formater()


if __name__ == '__main__':
    init(autoreset=True)
    formater()