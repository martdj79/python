import os

name = input('Введи имя: ')
print(" Привет,", name)
q = input("Ты хочешь поработать? Y/N: ")

if q == 'y' or q == 'Y':
    print("cooool!")
    print("Вот что я могу:")
    print("[1] - Выведу список файлов")
    print("[2] - А тут инфа о системе")
    do = int(input('Введи 1 или 2'))
    if do == 1:
        pass
    elif do == 2:
        pass
    else:
        pass
elif q == 'N' or q == 'n':
    print("ну и зря")
else:
    print("Шо?")
