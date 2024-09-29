import random

NUM_ROUNDS = 5

def get_user_guess():
    guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
    while guess not in ["higher", "lower"]:
        guess = input("Please enter 'higher' or 'lower': ").lower()
    return guess

def evaluate_guess(player_number, computer_number, guess):
    if player_number > computer_number and guess == "higher":
        return True
    elif player_number < computer_number and guess == "lower":
        return True
    elif player_number == computer_number:
        return None
    else:
        return False

def play_game():
    score = 0
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    for round_number in range(1, NUM_ROUNDS + 1):
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"Round {round_number}")
        print(f"Your number is {player_number}")
        
        guess = get_user_guess()

        result = evaluate_guess(player_number, computer_number, guess)

        if result is True:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        elif result is False:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        else:
            print(f"It's a tie! The computer's number was also {computer_number}. You don't earn a point this round.")

        print(f"Your score is now {score}\n")

    print("Thanks for playing!")
    final_message(score)

def final_message(score):
    if score == NUM_ROUNDS:
        print("Amazing! You got a perfect score!")
    elif score > NUM_ROUNDS / 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

play_game()