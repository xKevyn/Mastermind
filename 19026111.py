import random
def main():

	def Input2List(userInput1, userInput2, userInput3, userInput4):
		
		'''cant directly initialize userChoiceList = [userInput1, userInput2, userInput3, userInput4] becuase of the logic statement, 
		thus using this function as an initialization'''
		userChoicesList = [userInput1, userInput2, userInput3, userInput4]
		return userChoicesList
		
	def UserInput(Result):

		#if the user guess the colour correctly, remove the question
		if Result[0] != True:
			userInput1 = input('Please choose the first colour: ')
		else:
			userInput1 = randomColourChoices[0] #adding the answer to the user answer list once they got it right(only for easy mode)
		if Result[1] != True:
			userInput2 = input('Please choose the second colour: ')
		else:
			userInput2 = randomColourChoices[1]
		if Result[2] != True:
			userInput3 = input('Please choose the third colour: ')
		else:
			userInput3 = randomColourChoices[2]
		if Result[3] != True:
			userInput4 = input('Please choose the fourth colour: ')
		else:
			userInput4 = randomColourChoices[3]

		userChoicesList = Input2List(userInput1, userInput2, userInput3, userInput4)
		return userChoicesList
		
	#Showing the user the chosen set of colours
	def ChoicesDisplay(userChoicesList):

		DELIMETER = ', ' #constant
		#Lowercase the user input to avoid different represent of colour ex: [REd, Red, red, RED] and for uses in logic statements
		userChoices = DELIMETER.join([colour.lower() for colour in userChoicesList])
		print(f'Your choices are [{userChoices}]' )
		return userChoicesList    

	def Validator(Result):
		#display which oder of colour is guessed correctly(only for easy mode)
		if Result[0] == True:
			print('Your guess on the first colour is correct!')
		if Result[1] == True:
			print('Your guess on the second colour is correct!')
		if Result[2] == True:
			print('Your guess on the third colour is correct!')
		if Result[3] == True:
			print('Your guess on the fourth colour is correct!')
		

	def CCWPCalculation(randomColourChoices, userChoicesList, result):
		#create a temporary list for the random colour list
		tempList = randomColourChoices[:]
		#initialise variable for correct colour but wrong position 
		correctColourWrongPos = 0

		#check if the colour is in both list
		for i in userChoicesList:
			if i in tempList:
				tempList.remove(i) #remove the colour from the random colour list so that it wont be checked mroe than once
				correctColourWrongPos += 1
		correctColourWrongPos -= sum(result) #minus the correct colour and position
		return correctColourWrongPos

	#Identifying the correct pairs of guesses and display the position of the correct guesses
	def Guess(userChoicesList):

		result = [i == j for i, j in zip(userChoicesList, randomColourChoices)]
		correctColourNPosition = sum(result)
		correctColourWrongPos = CCWPCalculation(userChoicesList, randomColourChoices, result)
		print(f'Correct colour but wrong position: {correctColourWrongPos}')
		print(f'Correct colour in correct position: {correctColourNPosition}')
		Validator(result)
		return result

	def Hard():

		retry = 'yes'
		tries = 0
		result = [False, False, False, False]

		while sum(result) != 4 and retry == 'yes':
			#tries increase by 1 every time the user retries
			tries += 1
			
			#inputs			
			userInput1 = input('Please choose the first colour: ')
						
			userInput2 = input('Please choose the second colour: ')
		
			userInput3 = input('Please choose the third colour: ')

			userInput4 = input('Please choose the fourth colour: ')

			userChoicesList = [userInput1, userInput2, userInput3, userInput4]

			result = [i == j for i, j in zip(userChoicesList, randomColourChoices)]

			userChoices = ', '.join([colour.lower() for colour in userChoicesList])
			print(f'Your choices are [{userChoices}]' )

			correctColourNPosition = sum(result)

			correctColourWrongPos = CCWPCalculation(userChoicesList, randomColourChoices, result)

			#print(correctColourWrongPos) #debugging purposes

			print(f'Correct colour but wrong position: {correctColourWrongPos}')

			print(f'Correct colour in correct position: {correctColourNPosition}')

			print(f'Number of Tries: {tries}')     

			if sum(result) == len(randomColourChoices):
				print('Congratulation! you have guessed all the colour right')
				main()
			else:
				retry = input('Do you wanna try again? [Yes/No]: ')
				if retry.lower() == 'no':
					print(f'Too bad you did not got it right, the correct guesses are [{randomColourChoices}]')
					main()

	def Easy():

		retry = 'yes'
		tries = 0
		result = [False, False, False, False]

		while sum(result) != 4 and retry == 'yes':
			#tries increase by 1 every time the user retries
			tries += 1
			userChoicesList = UserInput(result)
			ChoicesDisplay(userChoicesList)
			result = Guess(userChoicesList)
			print('Number of Tries: ' + str(tries))	#display the total of tries	

			if sum(result) == len(randomColourChoices):
				#congratz the user and restart the program by going back to the main menu
				print('Congratulation! you have guessed all the colour right')
				main()
			else:
				retry = input('Do you wanna try again? [Yes/No]: ')
				if retry.lower() == 'no':
					print(f'Too bad you did not got it right, the correct guesses are [{randomColourChoices}]')
					main()

	def Help():

		#explaination of the game for the user
		helpMenu = input('-----------------Help Menu------------------\n/obj\n/typo\n/diff\n/menu (run this command to go back to the main menu)\nPlease enter the following commands\n')
		if helpMenu.lower() == '/obj':
			print('Objective of the game: \nGuess a secret code of colour consisting of a series of 4 colours.\nEach guess results in feedback narrowing down the possiblities of the code')
			Help()

		if helpMenu.lower() == '/typo':
			print('When the system display commands with "/", please include it in the input.\nOtherwise just type as the system shows, unless when guessing the colour which must input the first letter of the colour')
			Help()

		if helpMenu.lower() == '/diff':
			print('Easy mode will display a message when a guess is correct and permenantly remove the question for that round of guesses.\nHard mode will only tells the number of correct colour but wrong position guesses and correct colour and position guess')
			Help()

		if helpMenu.lower() == '/menu':
			main() #go back to the main menu

		else:
			print('There might be some typing errors, try including the symbol "/" ')
			Help()

	def error():

		#if there is typo, note the user and restart the program
		print('There might be some typing errors, try including the symbol "/" ')
		main() #restart the program

	def Difficulty():

		#prompt user to choose a difficulty
		difficulty = input('-----------------Difficulty------------------\nPlease select a difficulty\nEasy\nHard\n\nDifficulty: ')

		print('Four random colour sequence with replacement is generated...')

		#Explanation of the rules of the game to the user
		print('You are required to choose four colours from the given set of colours\n(repeated colour is allowed ex:[red, red, blue, green)')

		print('(Caution! please enter the first letter of the colour only)\n1. Red[R]\n2. Blue[B]\n3. Green[G]\n4. Pink[P]\n5. White[W]\n6. Orange[O]')		

		if difficulty.lower() == 'easy':
			Easy()		
			
		if difficulty.lower() == 'hard':
			Hard()
		
		else:
			error()

	mainMenu = input('-----------------Main Menu------------------\n/play\n/help (recommended if first time playing)\n/exit\n\nPlease enter the following commands: ')

	if mainMenu.lower() == '/play':

		#Generating the random sequence of colour from the list
		colourList = ['r', 'b', 'g', 'p', 'w', 'o']
		#Four random colour sequence with replacement is generated, ex:[red, red, green, green]
		randomColourChoices = random.choices(colourList, k = 4)
		#print(randomColourChoices) #debuging purposes
		Difficulty()

	if mainMenu.lower() == '/help':
		Help()

	if mainMenu.lower() == '/exit':
		exit() #exit the program
	else:
		error()

#run the main function
if __name__ == '__main__':
	main()

'''
improvemenmt of the program

make the whole program a class so that we can have a option to change the range of the random colour to guess

add a leaderboard feature 

prompt the user to enter a name for leaderboard purposes



'''
