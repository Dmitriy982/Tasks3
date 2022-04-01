def func():
    s = 1
    su = 0
    while s > 0:
        list1 = (input("Введите число через пробел или букву q для выхода из цилка: ").split())
        for i in list1:
            if i == "q":
                s = 0
            else:
                su = su + int(i)
                print(f"sum = {su}")


func()


