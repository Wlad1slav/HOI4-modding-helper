from PIL import Image
from colorama import init, Fore

def interface(directory, tag):
    z = '{'; x = '}'
    file = open(f'{directory}\interface\yor_icons.gfx', 'r')
    lines = file.readlines()
    lines[-1] = f"""    spriteType = {z} name = "{tag}_small"  texturefile = "gfx/flags/icons/icon_{tag}.dds" legacy_lazy_load = no {x}
{x}"""
    file.close()

    file = open(f'{directory}\interface\yor_icons.gfx', 'w')
    file.writelines(lines)
    file.close()


def functional(directory):
    tag = input("TAG: ")
    
    flag = Image.open(f"{directory}\gfx\\flags\{tag}.tga")
    flag = flag.resize((20, 13), Image.ANTIALIAS)
    flag.save(f"{directory}\gfx\\flags\icons\icon_{tag}.dds")

    print(f"{Fore.GREEN}{tag}{Fore.LIGHTGREEN_EX} готов\n")

    interface(directory, tag)
    functional(directory)


if __name__ == '__main__':
    init(autoreset=True)
    dir = input("Путь к папке мода: ")
    functional(dir)