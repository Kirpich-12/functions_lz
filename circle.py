from math import pi
usr_inp = input('Введите радиус:')

def squre(r:float) -> float: #Площадь окружности с заданным радиусом r
    sq = pi * (r ** 2)
    return sq
def lenth (r:float) -> float: #длинна окружности с заданным радиусом r
    ll = 2 * pi * r 
    return ll
print('Площадь круга с заданным радиусом:', squre(float(usr_inp)))
print('Длинна круга с заданным радиусом:', lenth(float(usr_inp)))

