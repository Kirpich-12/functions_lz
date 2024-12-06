usr_inp = input('Введите значение температуры по Цельсию:')

def temp_con(c:float) -> float: #Перевод температуры по Цельсию в температуру по Фаренгейту 
    fr = (c * (9/5)) + 32
    return fr

print('Температура в Фаренгейтах:', temp_con(float(usr_inp)))
