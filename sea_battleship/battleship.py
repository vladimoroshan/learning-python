from random import randint

class Board(object): 

	def __init__(self):
		self.board = []
		self.generate_board()

	def generate_board(self):
		for i in range(5):
			self.board.append([' o'] * 5)
	
	def get_board(self):
		return self.board


class Game(object):

	def __init__(self):
		self.computer_board = Board().get_board()	# Composition OOP
		self.computer_ship_row = randint(0, len(self.computer_board)-1)
		self.computer_ship_col = randint(0, len(self.computer_board[0])-1)

		self.human_board = Board().get_board() # Composition OOP
		self.human_ship_row = int(input("On which 'row' do you want to place your ship? [0-4]:"))
		self.human_ship_col = int(input("On which 'col' do you want to place your ship? [0-4]:"))
		self.human_board[self.human_ship_row][self.human_ship_col] = ' s'

		self.human_turn = True
		self.start()

	def print_board(self):
		print("\n")
		print("="*50)
		print("Human's ocean")

		for i in self.human_board:
			print(' '.join(i))

		print("Computer's ocean")

		for i in self.computer_board:
			print(' '.join(i))

		print("="*50)

	def start(self):
		print("\n\n\n\n\n\n\n\n\n\nLet's play Battleship!")
		print("Be the first to sink the enemy's ship!")

		while True:	

			if self.human_turn:				
				self.print_board()
				guess_row = int(input('Guess Row [0-4]:'))
				guess_col = int(input('Guess Col [0-4]:'))

				if guess_row == self.computer_ship_row and guess_col == self.computer_ship_col:
					print("Congratulations. You won!")
					break
				elif (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
					print("Opps, that's not even in the ocean. Try again")
				elif self.computer_board[guess_row][guess_col] == ' x':
					print('You shoot that one already')
				else:
					print("You missed.")
					self.computer_board[guess_row][guess_col] = ' x'

				self.human_turn = not self.human_turn	# Flip to a False

			else:	# Computer's turn
				guess_row = randint(0, len(self.human_board)-1)
				guess_col = randint(0, len(self.human_board[0])-1)
				if self.human_board[guess_row][guess_col] == ' s':
					print("Computer won")
					print("Game over!")
					break
				else:
					print("Computer missed")
					self.human_board[guess_row][guess_col] = ' x'

				self.human_turn = not self.human_turn	# Flip to a True

my_game = Game()
