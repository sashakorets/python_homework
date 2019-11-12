"""
------------------------------------
Користувач уводить три числа. 
Збільшити перше число в два рази,
друге числа зменшити на 3, 
третє число звести в квадрат і
потім знайти суму нових трьох чисел.
------------------------------------
"""

import re
from validators.validator import validator
from validators.start_info_about_me import start_info

start_info()

k = '1'
while k == '1':
    re_float = re.compile("^[-+]{0,1}\d*\.{0,1}\d+$")

    x = float(validator(re_float,'Number one:'))
    y = float(validator(re_float,'Number two:'))
    z = float(validator(re_float,'Number three:'))
    x = x * 2
    y = y - 3
    z = pow(z, 2)
    print('Number one*2: ',x)
    print('Number two-3: ',y)
    print('Number three^2: ',z)
    print('Number one*2+Number two-3+Number three^2: ',x+y+z)
    k = input('**********************************\nВиконати програми ше раз - 1\nЗакінчити роботу - інший символ\n**********************************')