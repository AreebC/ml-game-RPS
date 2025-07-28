import random
from sklearn.naive_bayes import MultinomialNB
from collections import deque
import numpy as np

# Encode moves
move_to_num = {'rock': 0, 'paper': 1, 'scissors': 2}
num_to_move = {0: 'rock', 1: 'paper', 2: 'scissors'}

# History tracking
history_length = 2
player_history = deque(maxlen=history_length)
X = []
y = []

model = MultinomialNB()

def encode_sequence(seq):

    return [move_to_num[m] for m in seq]



def predict_next_move():

    if len(X) < 5:

        return random.choice(['rock', 'paper', 'scissors'])



    input_seq = np.array(encode_sequence(player_history)).reshape(1, -1)

    predicted = model.predict(input_seq)[0]

    return num_to_move[(predicted + 1) % 3]  # counter move



def update_model():

    if len(player_history) == history_length + 1:

        features = encode_sequence(list(player_history)[:-1])

        label = move_to_num[player_history[-1]]

        X.append(features)

        y.append(label)

        model.fit(np.array(X), np.array(y))



def play_game():

    print("Let's play Rock Paper Scissors (ML mode). Type 'exit' to quit.")

    while True:

        player_move = input("Your move (rock, paper, scissors): ").lower()

        if player_move == 'exit':

            break

        if player_move not in move_to_num:

            print("Invalid move. Try again.")

            continue



        player_history.append(player_move)

        update_model()



        ai_move = predict_next_move()

        print(f"AI chooses: {ai_move}")



        if ai_move == player_move:

            print("It's a tie!")

        elif (ai_move == 'rock' and player_move == 'scissors') or \
             (ai_move == 'scissors' and player_move == 'paper') or \
             (ai_move == 'paper' and player_move == 'rock'):

            print("AI wins!")

        else:

            print("You win!")



if __name__ == "__main__":

    play_game()