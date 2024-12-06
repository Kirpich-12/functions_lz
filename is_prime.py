usr_int = int(input('Введите число: '))


def prime(n:int) -> str:
    d = 2
    while (d ** 2) <= n and n % d != 0:
        d += 1
    if (d ** 2) > n:
        ans = 'Число простое'
    else:
        ans = 'Число сложное'
    return ans


print(prime(usr_int))

