usr_inp = input('Введите хоть что-нибудь ')

def palindrom(a):
    x = len(a)
    i = 0
    x = x - 1
    k = 0
    while x - i >= i:
        if a[x - i] == a[i]:
            i += 1
        else:
            k = 1
            break
    if k == 1:
        ans = 'Не палиндром'
    else:
        ans = 'Палиндром'
    return ans

print(palindrom(usr_inp))