from random import randint

def hangman():
	words = ['boolean', 'language', 'debugger', 'developer', 'software']

	guess_word = list(words[randint(0, len(words)-1)].upper()) 
	guessed_letters = ["_"]*len(guess_word) # Repetition of '_' by length of the word
	missed_letters = set() # To remove a letter if a player typed it again

	while True:
		if len(missed_letters) > 9:
			print("Game over!")
			break
		else:
			print("\n\n\n\nWord:", ' '.join(guessed_letters))
			print("Misses:", ', '.join(missed_letters))	
			user_input = input("Guess: ").upper()		

			if isinstance(user_input, str) and len(user_input) == 1: # if str and only 1 letter
				if user_input in guess_word:
					for i in range(len(guess_word)):
						if guess_word[i] == user_input:				
							guessed_letters[i] = user_input

					if guess_word == guessed_letters:
						print("Win! The word was ", ' '.join(guess_word))
						break			
							
				else: 
					missed_letters.add(user_input.lower())	

hangman()
