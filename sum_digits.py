usr_inp = int(input('Введите число: '))

def summ(ch:int) -> int: #Полсчёт всез цифр в числе 
    ch = str(ch)
    ans = 0
    for i in range(len(ch)):
        ans += int(ch[i])
    return ans 

print('Сумма всех чисел в числе: ', summ(usr_inp))