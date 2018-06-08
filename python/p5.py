def check (a) :
	try :
		a = int(a)
		if a % 2 == 0 :
			print('EVEN')
		else :
			print('ODD')
	
	
	except ValueError as e:
		print('Entered value is not a number Not a number')
	except NameError as e:
		print('Entered value is not a number Not a number')
	except TypeError as e:
		print('Entered value is not a number Not a number')
