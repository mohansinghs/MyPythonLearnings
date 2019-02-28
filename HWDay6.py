try:
    a = int(input('Enter First Numerical Value:-  '))
except ValueError as error:
    print('Im Sorry I cano\'t convert string')
try:
    b = int(input('Enter Second Numerical Value:-  '))
    print('1st Number:{0}, 2nd Number:{1}\nAdd:{2}\nSubtract:{3}\nMultiply:{4}\nDivide:{5}\nPercent:{6}\nPower:{7}'.format(a, b, (a + b), (a - b), (a * b),
                                                                                      (a / b), (a % b), (a ** b)))
except ValueError as error:
    print('Im Sorry I cano\'t convert string')

