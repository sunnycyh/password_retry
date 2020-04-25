password = 'a123456'
chance = '3'
chance = int(chance)
while chance > 0:
	chance = chance - 1
	pw = input('Please enter the password: ')
	if password == pw:
		print('Login success!')
		break
	else:
		print('Wrong password!')
		if chance > 0:
			print('You have', chance, 'more chances!')
		else:
			print('Your account would be locked in the coming 24 hours!')