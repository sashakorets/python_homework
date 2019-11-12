'''
***************
n
---
\   (x+i)/i   це умова задачі
/
---
i=1
***************
'''

import re
from validators.validator import validator
from validators.start_info_about_me import start_info

re_integer = re.compile("^[-+]{0,1}\d+$")
re_float = re.compile("^[-+]{0,1}\d*\.{0,1}\d+$")

start_info()

k = '1'
while k == '1':
    def SumaOfSameRivniannia(data_equation):
        '''

        :param data_equation: (text) but this parameter must meet the standards python
        :return: (float)
        '''
        n = int(validator(re_integer, 'Введіть n :'))
        x = float(validator(re_float, 'Введіть x :'))
        sum_end = float(0)
        for i in range(1, n + 1):
            sum = eval(data_equation)
            sum_end = sum + sum_end
            i += 1
        resust = 'suma first {0} chleniv= {1}'.format(n, sum_end)
        return resust
    print('***************\nn\n---\n\   (x+i)/i\n/\n---\ni=1\n***************')
    print(SumaOfSameRivniannia('(x+i)/i'))
    k = input('**********************************\nВиконати програми ше раз - 1\nЗакінчити роботу - інший символ\n**********************************')