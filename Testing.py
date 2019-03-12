try:
    a = float(input('Enter First Value:-  '))
    b = float(input('Enter Second Value:-  '))
    operation = input('Enter operator as per list only = (+,-,*,^,%,/)')
    if operation == '+':
        print(a+b)
    elif operation == '-':
        print(a-b)
    elif operation == '*':
        print(a*b)
    elif operation == '^':
        print(pow(a, b))
    elif operation == '%':
        if b == 0:
            print('Oops second value is \'Zero\'. Denominator can\'t be is Zero.')
        else:
            print(a % b)
    elif operation == '/':
         if b == 0:
            print('Oops second value is \'Zero\'. Denominator can\'t be is Zero.')
         else:
            print(a/b)
    else:
        print('select accurate operation from list')
except ValueError as error:
    print('Wrong Input, please enter only digit')


