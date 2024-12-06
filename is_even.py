usr_inp = int(input('Введите число: '))

def isit(ch:int) -> str: #Проверка на чётность 
    if ch % 2 == 0:
        ans = 'Введенное число чётное'#Ответ в слуае чётности
    else:
        ans = 'Введённое число нечётное'#Ответ в случае нечётности 
    return ans

print(isit(usr_inp))
