try:
    a = float(input('Enter First Numerical Value:-  '))
except ValueError as error:
    print('Im Sorry I cano\'t convert string')
try:
    b = float(input('Enter Second Numerical Value:-  '))
    print(
        '1st Number:{0:.5f}, 2nd Number:{1:.5f}\nAdd:{2:.5f}\nSubtract:{3:.5f}\nMultiply:{4:.5f}\nDivide:{5:.5f}'
        '\nPercent:{6:.5f}\nPower:{7:.5f}'.
            format(a, b, (a + b), (a - b), (a * b), (a / b), (a % b), (a ** b)))
except ValueError as error:
    print('Im Sorry I cano\'t convert string')
