import random
def main():

	def Input2List(userInput1, userInput2, userInput3, userInput4):
		
		userChoicesList = [userInput1, userInput2, userInput3, userInput4]
		return userChoicesList
		
	def UserInput(Result):
	   
		userQuestion = 'from below\n(tips: enter the first letter of the colour)\n1. Red[R]\n2. Blue[B]\n3. Green[G]\n4. Pink[P]\n5. White[W]\n6. Orange[O]\nColour: '
		
		if Result[0] != True:
			userInput1 = input("Please choose the first colour " + userQuestion)
		else:
			userInput1 = randomColourChoices[0]
		if Result[1] != True:
			userInput2 = input("Please choose the second colour " + userQuestion)
		else:
			userInput2 = randomColourChoices[1]
		if Result[2] != True:
			userInput3 = input("Please choose the third colour " + userQuestion)
		else:
			userInput3 = randomColourChoices[2]
		if Result[3] != True:
			userInput4 = input("Please choose the fourth colour " + userQuestion)
		else:
			userInput4 = randomColourChoices[3]

		userChoicesList = Input2List(userInput1, userInput2, userInput3, userInput4)
		return userChoicesList
		
	#Showing the user the chosen set of colours
	def ChoicesDisplay(userChoicesList):
		
		#Lowercase the user input to avoid different represent of colour ex: [REd, Red, red, RED] and for uses in logic statements
		userChoices = ', '.join([colour.lower() for colour in userChoicesList])
		print('Your choices are [' + userChoices + ']' )
		return userChoicesList    

	def Validator(Result):
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
		tempAns = randomColourChoices[:]
		#initialise variable for correct colour but wrong position 
		correctColourWrongPos = 0

		#check if the colour is in both list
		for i in userChoicesList:
			if i in tempAns:
				tempAns.remove(i) #remove the colour from the random colour list so that it wont be checked mroe than once
				correctColourWrongPos += 1
		correctColourWrongPos -= sum(result) #minus the correct colour and position
		return correctColourWrongPos

	#Identifying the correct pairs of guesses and display the position of the correct guesses
	def Guess(userChoicesList):

		Result = [i == j for i, j in zip(userChoicesList, randomColourChoices)]
		correctColourNPosition = sum(Result)
		correctColourWrongPos = CCWPCalculation(userChoicesList, randomColourChoices, result)
		print('Correct colour but wrong position: ' + str(len(correctColourWrongPos)))
		print('Correct colour in correct position: ' + str(correctColourNPosition))
		Validator(Result)
		return Result

	mainMenu = input('-----------------Main Menu------------------\n/play\n/help\n/exit\nPlease enter the following code\n')

	if mainMenu.lower() == '/play':
		#Generating the random sequence of colour from the list
		colourList = ['r', 'b', 'g', 'p', 'w', 'o']
		#Four random colour sequence with replacement is generated, ex:[red, red, green, green]
		randomColourChoices = random.choices(colourList, k = 4)
		print(randomColourChoices) #debuging purposes

		print('Four random colour sequence with replacement is generated...')

		#Explanation the rules of the game to the user
		print('You are required to choose four colours from the given set of colours(repeated colour is allowed ex:[red, red, blue, green)')

		difficulty = input('Please select a difficulty\nEasy\nHard\n\nDifficulty: ')

		if difficulty.lower() == 'easy':

			retry = 'yes'
			tries = 0
			result = [False, False, False, False]

			while sum(result) != 4 and retry == 'yes':
				tries += 1
				userChoicesList = UserInput(result)
				ChoicesDisplay(userChoicesList)
				result = Guess(userChoicesList)
				print('Number of Tries: ' + str(tries))		

				if sum(result) == 4:
					print('Congratulation! you have guessed all the colour right')
					main()
				else:
					retry = input('Do you wanna try again? [Yes/No]: ')

		if difficulty.lower() == 'hard':

			retry = 'yes'
			tries = 0
			result = [False, False, False, False]

			while sum(result) != 4 and retry == 'yes':
				tries += 1
				
				userQuestion = 'from below\n(tips: enter the first letter of the colour)\n1. Red[R]\n2. Blue[B]\n3. Green[G]\n4. Pink[P]\n5. White[W]\n6. Orange[O]\nColour: '
			
				userInput1 = input("Please choose the first colour " + userQuestion)
							
				userInput2 = input("Please choose the second colour " + userQuestion)
			
				userInput3 = input("Please choose the third colour " + userQuestion)

				userInput4 = input("Please choose the fourth colour " + userQuestion)

				userChoicesList = [userInput1, userInput2, userInput3, userInput4]

				result = [i == j for i, j in zip(userChoicesList, randomColourChoices)]

				userChoices = ', '.join([colour.lower() for colour in userChoicesList])
				print('Your choices are [' + userChoices + ']' )

				correctColourNPosition = sum(result)

				correctColourWrongPos = CCWPCalculation(userChoicesList, randomColourChoices, result)

				#print(correctColourWrongPos)

				print('Correct colour but wrong position: ' + str(correctColourWrongPos))

				print('Correct colour in correct position: ' + str(correctColourNPosition))

				print('Number of Tries: ' + str(tries))     

				if sum(result) == 4:
					print('Congratulation! you have guessed all the colour right')
					main()
				else:
					retry = input('Do you wanna try again? [Yes/No]: ')


	if mainMenu.lower() == '/help':
		helpMenu = input('-----------------Help Menu------------------\n/rule\n/help\n/exit\nPlease enter the following code\n')

	if mainMenu.lower() == '/exit':
		exit()
	else:
		print('There might be some typing errors, try including the symbol "/" ')
		main()

if __name__ == '__main__':
	main()

