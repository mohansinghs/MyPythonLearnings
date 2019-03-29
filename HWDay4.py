print('Enter your details in below fields')                       # quotes used for printing instruction for user
name = input('Enter Name:- ')                                     # always use for getting information from user
sbu = input('Enter SBU:- ')
print('If you want to change SBU please enter new SBU')
sbu = input('Enter New SBU:- ')
print('Your SBU is changed successfully check below')
print('\033[1m' + ' Name:- {0}'.format(name))
print('SBU:-{0}'.format(sbu))                                       # to override never create new input