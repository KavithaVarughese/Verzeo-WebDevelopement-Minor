class Error(Exception):
	pass

class NotCharacter(Error):
	pass

class NotValidAge(Error):
	pass

def create() :
	with open('user.txt', 'w') as f:
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
		f.write(name + '\n')
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
		age= str(age)
		f.write(age + '\n')

def display() :
	with open ('user.txt' , 'r') as f:
		print('Name : ', f.readline())
		print('Age : ',f.readline())

print('1. Create \n2. Display \n3.Exit')
ch = 0
while ch!=3:
	ch = int(input('enter your choice : '))
	if ch == 1 :
		create()
	elif ch==2:
		display()
	elif ch==3:
		continue;
	else:
		print('wrong choice')

