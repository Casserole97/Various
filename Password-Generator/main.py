import secrets, string

sys_rand = secrets.SystemRandom

lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
digits = list(string.digits)

choice = secrets.choice


def passwordnew(x, password_name='Password:'):
	'''Create a new password, with 'x' being the number of symbols'''
	newpassword = []
	for i in range(x):
		a = choice([1, 2, 3])
		if a == 1:
			newpassword.append(choice(lowercase))
		if a == 2:
			newpassword.append(choice(uppercase))
		if a == 3:
			newpassword.append(choice(digits))

	passwordfinished = ''.join(newpassword)

	passwords_file = open(str('passwords.txt'), 'a')
	passwords_file.write(password_name + '\n' + passwordfinished + '\n' * 2)
	passwords_file.close()

	print(passwordfinished)


passwordnew(24)
