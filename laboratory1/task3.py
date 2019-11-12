"""
----------------------------
Прогарма виконує функцію
вказану нижче
----------------------------
F(x)={0,       якщо x<=1
     {1/(x+6), якщо x>1
----------------------------
Ведіть дійсне число
----------------------------
"""

import re
from validators.validator import validator
from validators.start_info_about_me import start_info

start_info()

re_float = re.compile("^[-+]{0,1}\d*\.{0,1}\d+$")
k = '1'
while k == '1':
    data_number = float(validator(re_float,'your number:'))
    if data_number > 1:
        print(1 / (data_number + 6))
    else:
        print(0)
    k = input('**********************************\nВиконати програми ше раз - 1\nЗакінчити роботу - інший символ\n**********************************')