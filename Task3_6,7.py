def int_func():
    s = 1
    while s > 0:
        list1 = (input("\nВведите слово через пробел или цифру 1 для выхода из цилка: ").split())
        for i in list1:
            if i == "1":
                s = 0
            else:
                str1 = str(i.capitalize())
                print(str1, end=' ')


int_func()

