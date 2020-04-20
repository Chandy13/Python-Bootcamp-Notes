## This program will calculate a user's gross Salary or Hourly wage. 

## Start by asking user for option between calculating hourly wage or yearly pay

def what_to_calculate():

	#Ask initial question
	init_question = input('What would you like to calculate, hourly wage or yearly salary? ')

	#Start loop to confirm answer
	while True:
		if init_question[0].lower() == 'h':
			return 'hr'
			break
		elif init_question[0].lower() == 'y':
			return 'yr'
			break
		else:
			init_question = input('Please enter either h for hourly wage or y for yearly salary, I cannot do anything else as of now: ')

## Create Object to store entered information

class Wage:

	def __init__(self,h_amount=0,y_amount=0,vac_pay=0, bonus=0, hours=0):

		#h_amount is hourly wage entered
		self.h_amount = h_amount

		#y_amount is yearly wage entered
		self.y_amount = y_amount
		
		#vac_pay is vacation rate (entered as a percentage)
		self.vac_pay = vac_pay

		#bonus is amount of bonus paid in lump sum
		self.bonus = bonus

		#hours is number of hours worked in a week
		self.hours = hours

## Create function to ask user to enter information

def input_info(choice, user):

	#Start by asking for hours
	while True:
		user.hours = input('How many hours do you work per week? ')
		try:
			float(user.hours) * 0 == 0
		except:
			print('Please enter numbers, I do not like letters!!!!!')
			continue
		else:
			user.hours = float(user.hours)
			break

	#Next is asking for bonus rate
	while True:
		user.vac_pay = input('What is your vacation rate, if you dont have one then enter 1: ')
		try:
			float(user.vac_pay) * 0 == 0
		except:
			print('Please enter numbers, I do not like letters!!!!!')
			continue
		else:
			user.vac_pay = float(user.vac_pay)
			break

	#Finally ask for bonus
	while True:
		user.bonus = input('Do you receive a bonus? Please add it up to a yearly value and enter it here: ')
		try:
			float(user.bonus) * 0 == 0
		except:
			print('Please enter numbers, I do not like letters!!!!!')
			continue
		else:
			user.bonus = float(user.bonus)
			break

	#Choice of question depends on variable Choice which should equal either a string of hr or yr

	#Asks for HOURLY wage if user wants to calculate Yearly
	if choice == 'yr':
		while True:	
			user.h_amount = input('Please enter your hourly wage: ')
			try:
				float(user.h_amount) * 0 == 0
			except:
				print('Please enter numbers, I cannot understand letters!')
				continue
			else:
				user.h_amount = float(user.h_amount)
				break

	#Asks for YEARLY wage if user wants to calculate Hourly
	if choice == 'hr':
		while True:	
			user.y_amount = input('Please enter your yearly wage: ')
			try:
				float(user.y_amount) * 0 == 0
			except:
				print('Please enter numbers, I cannot understand letters!')
				continue
			else:
				user.y_amount = float(user.y_amount)
				break

## Create final function to calculate

def Pay_Calculator():
	
	#Set user object up
	user = Wage()

	#Welcome user
	print('Welcome to the Pay Calculator created by Chanda!')
	input('Press Enter to start!')
	print(' ')

	#Asks for info
	input_info(what_to_calculate(),user)

	if user.h_amount == 0:
		if user.bonus == 0:
			user.h_amount = round(user.y_amount / 52 / user.hours, 2)
		else:
			user.h_amount = round((user.y_amount + user.bonus) / 52 / user.hours, 2)

	if user.y_amount == 0:
		user.y_amount = round(user.h_amount * user.vac_pay * user.hours * 52 + user.bonus, 2)

	print(' ')
	print(f'Your hourly wage is ${user.h_amount} \nYour yearly wage is ${user.y_amount}')

## Run the final function

Pay_Calculator()

## Add the __main__ commands to confirm the running of this if this is main script that is run