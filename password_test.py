password = 'a123456'
chance = '3'
chance = int(chance)
while chance > 0:
	pw = input('Please enter the password: ')
	if password == pw:
		print('Login success!')
		break
	else:
		chance = chance - 1
		print('Wrong password, you have', chance, 'more chances!')
		