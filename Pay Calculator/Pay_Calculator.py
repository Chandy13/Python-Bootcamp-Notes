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

	def __init__(self, h_amount=0,y_amount=0, vac_pay=0, bonus=0):

		#h_amount is hourly wage entered
		self.h_amount = h_amount

		#y_amount is yearly wage entered
		self.y_amount = y_amount
		
		#vac_pay is vacation rate (entered as a percentage)
		self.vac_pay = vac_pay

		#bonus is amount of bonus paid in lump sum
		self.bonus = bonus

## Create function to ask user to enter information

## Create final function to calculate

## Run the final function

## Add the __main__ commands to confirm the running of this if this is main script that is run