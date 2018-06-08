
class Error(Exception):
	pass

class NotCharacter(Error):
	pass

class NotValidAge(Error):
	pass

while True:
	global name 
	name = input('Enter you name: ')
	try:
		for letter in name :
			if ((letter < 'a') | (letter > 'z') )& ((letter < 'A') | (letter > 'Z')):
				raise NotCharacter('There is an unknown character in you name')

	except NotCharacter as e:
		print(e)
		print('please type name again')
		continue

	else:
		check = input('Change due to spelling mistake (y/n) : ')
		if check == 'y' : 
			continue
		break

while True :
	try :
		global age 
		age = int(input('enter your age : '))

	except ValueError as e:
		print('Not a number')
		print(' Please enter age again : ')
		continue
	else:
		check = input('Any change in age ? (y/n) : ')
		if check == 'y' : 
			continue
		break

print ('Name : ' + name)
print('Age : ', end='')
print(age)