print('Enter your details in below fields')                       # quotes used for printing instruction for user
name = input('Enter Name:- ')                                     # always use for getting information from user
sbu = input('Enter SBU:- ')
print('Information entered by you are as follow')
print('Name:-',name)
print('SBU:-',sbu)
print('If you want to change SBU please enter new SBU')
sbu1 = input('Enter New SBU:- ')
print('New SBU is {0} & your old SBU was {1}'.format(sbu1,sbu))