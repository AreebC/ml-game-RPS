import random
from sklearn.naive_bayes import MultinomialNB

# Encode choices
choices = ['rock', 'paper', 'scissors']
choice_to_number = {'rock': 0, 'paper': 1, 'scissors': 2}
number_to_choice = {v: k for k, v in choice_to_number.items()}

# ML setup
X = [] # Features (last moves)
y = [] # Labels (next move)
model = MultinomialNB()

def get_computer_move(user_history):
	if len(X) >= 5:
		model.fit(X, y)
		prediction = model.predict([user_history[-1]])[0]
		return (prediction + 1) % 3  # Counter predicted user move
	else:
		return random.randint(0, 2)

def play_round():
	user_input = input("Enter rock, paper, or scissors (or 'quit'): ").lower()
	if user_input == 'quit':
		return False

	if user_input not in choice_to_number:
		print("Invalid input. Try again.")
		return True

	user_move = choice_to_number[user_input]

	if len(X) == 0:
		comp_move = random.randint(0, 2)
	else:
		comp_move = get_computer_move(X)

	print(f"Computer chose: {number_to_choice[comp_move]}")

	if comp_move == user_move:
		print("It's a tie!")
	elif (user_move - comp_move) % 3 == 1:
		print("You win!")
	else:
		print("You lose!")

	# Store feature and label
	X.append([user_move])
	y.append(user_move)

	return True

# Game loop
print("=== Rock Paper Scissors (ML) ===")
while True:
	if not play_round():
		break