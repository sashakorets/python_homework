'''
-------------------------------------
Організувати безперервне введення
цілих чисел з клавіатури, поки
користувач не введе задане число t. Після
введення t, показати на екрані кількість
чисел, які були введені, їх загальну
суму і середнє арифметичне.
-------------------------------------
'''

import re
from validators.validator import validator
from validators.start_info_about_me import start_info

re_integer = re.compile("^[-+]{0,1}\d+$")
re_float = re.compile("^[-+]{0,1}\d*\.{0,1}\d+$")

def FuncForSecondTask(stop_simvol):
    '''
        function creates a loop that allows you to continuously enter integers until you enter a special(:param stop_simvol) character
    :param stop_simvol: (int)
    :return: sum (int) all chleniv without last(:param stop_simvol),kilkist (int) all chleniv without last(:param stop_simvol),ser_arefmetic or sum/kilkist (float)
    '''
    sum = 0
    kilkist = 0
    i = None
    while i != stop_simvol:
        i = float(validator(re_float, 'Введіть число :'))
        kilkist += 1
        sum = i + sum
    return  sum-stop_simvol,kilkist-1,(sum-stop_simvol)/(kilkist-1)


start_info()



k = '1'
while k == '1':
    t = float(validator(re_float, 'Введіть закриваюче ціле число "t": '))
    result_sum, kilkist, ser_arefmetic = (FuncForSecondTask(t))
    print('*******************\nsum all numbers without last: {}\nkilkist all numbers without last: {}\nthe atithmetic mean: {}\n*******************'.format(result_sum, kilkist, ser_arefmetic))
    k = input('**********************************\nВиконати програми ше раз - 1\nЗакінчити роботу - інший символ\n**********************************')