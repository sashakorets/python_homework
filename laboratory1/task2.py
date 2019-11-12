"""
--------------------------------
Увести з клавіатури дійсні
числа х і у, не рівні одне
одному. Менше з цих двох чисел
замінити половиною їх суми,
а більше - їх подвоєним добутком.
---------------------------------
"""

import re
from validators.validator import validator
from validators.start_info_about_me import start_info

start_info()

k = '1'
while k == '1':
    def StrictInequality(a,b):
        '''
            func returne :param a and :param b if a!=b, else funс asks to enter again
        :param a:(float)
        :param b:(float)
        :return: (:param a),(:param b)
        '''
        re_float = re.compile("^[-+]{0,1}\d*\.{0,1}\d+$")
        A = float(validator(re_float, a))
        B = float(validator(re_float, b))
        while A==B:
            A = float(validator(re_float, 'same number 1 : '))
            B = float(validator(re_float, 'same number 2 : '))
        else:
            return A,B

    x,y = StrictInequality('same number 1 :','same number 2 :')
    print('x = ',x,'\ny = ',y)
    if x > y:
        y1 = (x + y) / 2
        print('y менше чим x, y=(x+y)/2=',y1)
        x1 = x * y * 2
        print('x більше чим y, x=y*x*2=',x1)
    else:
        x2 = (x + y) / 2
        print('x менше чим y, x=(x+y)/2=',x2)
        y2 = x * y * 2
        print('y більше чим x, y=y*x*2=',y2)
    k = input('**********************************\nВиконати програми ше раз - 1\nЗакінчити роботу - інший символ\n**********************************')