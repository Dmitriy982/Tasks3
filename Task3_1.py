def div(arg1, arg2):
    if arg2 == 0:
        return 'error'
    else:
        res = arg1 / arg2
        return res


print(div(int(input("Введите первое число: ")), (int(input("Введите первое число: ")))))
