from PIL import Image
import os
# 41x26

def functional(x, y):
    files = os.listdir('D:\HoiModding\YOR\gfx\\flags\icons')
    flags = filter(lambda x: x.endswith('.dds'), files)

    for flag in flags:
        img = Image.open(f"D:\HoiModding\YOR\gfx\\flags\icons\{flag}")
        img = img.resize((x, y), Image.ANTIALIAS)
        img.save(f"D:\HoiModding\YOR\gfx\\flags\icons\{flag}")


if __name__ == '__main__':
    x = int(input("x: "))
    y = int(input("y: "))
    functional(x, y)