
is_restricted = True
is_high_salary = False

def bank_account_open():
	print(' Full Name: ')
	name = input()
	print(' Salary: ')
	salary = input()
	#casting, str input to int
	if( int(salary) > 5000 ):
		is_high_salary = True
	bank_status(is_high_salary, name)

def bank_status(is_high_salary, name ):
	#formating string
	print(f'{name}, Allow for Bank Account')

bank_account_open()