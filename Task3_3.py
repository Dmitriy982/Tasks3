def my_func(arg1, arg2, arg3):
    a = min(arg1, arg2, arg3)
    res = arg1 + arg2 + arg3 - a
    return res


print(my_func(int(input("Первое число: ")), (int(input("Второе число: "))), (int(input("Третье число: ")))))