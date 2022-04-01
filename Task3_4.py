def my_func(x, y):
    if x <= 0 | y >= 0:
        return 'Wrong numbers'
    else:
        a = 1
        res = x ** y  # Первый способ
        for i in range(abs(y)):
            a = x * a
        res1 = 1 / a  # Второй способ
        return res1, res


print(my_func(2, -4))
