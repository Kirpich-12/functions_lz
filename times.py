usr_inp = input('Введите время в формате hr-min-sec')

def time_to_sec(tm:str) -> int:
    sec = 0
    tm_list = tm.split('-')
    sec = (int(tm_list[0]) * 3600) + (int(tm_list[1]) * 60) + int(tm_list[2])
    return sec

print('Количество секунд:', time_to_sec(usr_inp))