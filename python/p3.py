# Simple Calculator

def add(a,b):
	c= a+b
	return (c)

def sub(a,b):
	c= a-b
	return(c)

def mul(a,b):
	c= a*b
	return (c)

def div(a,b):
	c= a/b
	return c

choice = 'y'

while choice == 'y':

	while True :	
		try :
			global x
			 
			x= int(input("Enter the first number: "))
			

		except ValueError as e:
			print('Not a number')
			print(' Please enter first number again : ')
			continue
		else :
			break

	while True :	
		try :
			
			global y 
			
			y= int(input("Enter the second number: "));

		except ValueError as e:
			print('Not a number')
			print(' Please enter second number again : ')
			continue
		else:
			break

	while True :	
		op = input("Select ( + | - | * | / ) : ")
		if(op=='+'):
			print(add(x,y))
			break
		elif (op=='-'):
			print(sub(x,y))
			break
		elif(op=='*'):
			print(mul(x,y))
			break
		elif(op=='/'):
			if(y==0):
				print("indefined")
				break
			else:
				print(div(x,y))
				break
		else:
			print("invalid operation")		
			continue

	choice = input('Do you want to do another calculation ? (y/n) : '  )