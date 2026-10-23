# Multi Player Quiz
# Walk Through of the Quiz
# 2 players are added using the input function
# Player 1 is asked the questions, and a score is kept
# Player 2 is asked the questions, and a score is kept
# The scores are compared and the winner is displayed.
# The questions are hardcoded as below
    # "What is the chemical symbol for water?", ["CO2", "O2", "H2O", "NaCl"], "H2O"
    # "Which planet is known as the Red Planet?", ["Venus", "Jupiter", "Saturn", "Mars"], "Mars"
    # "What is the square root of 64?", ["6", "7", "8", "9"], "8"
    # "How many colors are there in a standard rainbow?", ["5", "6", "7", "8"], "7"
    # "Which animal is known as the King of the Jungle?", ["Elephant", "Tiger", "Bear", "Lion"], "Lion"

# first of all, we have three entities:
# 1. player: attributes are name and score is 0 > we create this and its constructor > done
# 2. question: we have question: str, options: list, answer: str
# 3. quiz: quiz, takes in a list of questions and a list of players. now, list of questions is hardcoded.
from questions import Question
from player import Player
from quiz import Quiz

question_list = [
    Question("What is the chemical symbol for water?", ["CO2", "O2", "H2O", "NaCl"], "H2O"),
    Question("Which planet is known as the Red Planet?", ["Venus", "Jupiter", "Saturn", "Mars"], "Mars"),
    Question("What is the square root of 64?", ["6", "7", "8", "9"], "8"),
    Question("How many colors are there in a standard rainbow?", ["5", "6", "7", "8"], "7"),
    Question("Which animal is known as the King of the Jungle?", ["Elephant", "Tiger", "Bear", "Lion"], "Lion")
]

player_list = []
def add_player():
    player_name = input("Enter the name of the player: ")
    player_name = Player(player_name)
    player_list.append(player_name)
    print("Player added..")

add_player()
add_player()

new_quiz = Quiz(player_list, question_list)
new_quiz.run_quiz()
new_quiz.show_result()