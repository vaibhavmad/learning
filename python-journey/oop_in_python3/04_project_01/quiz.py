class Quiz:
    def __init__(self, players: list, questions: list):
        self.players = players
        self.questions = questions

    def run_quiz(self):
        for player in self.players:
            print(player.name)
            for question in self.questions:
                print(question.question)
                print("Options are:")
                for option in question.options:
                    print(option)
                prompt = input("\nYour answer: ")
                if prompt.lower() == question.answer.lower():
                    player.score += 1

    def show_result(self):
        player_1_name = self.players[0].name
        player_2_name = self.players[1].name
        player_1_score = self.players[0].score
        player_2_score = self.players[1].score
        print(f"{player_1_name}'s score is: {player_1_score}")
        print(f"{player_2_name}'s score is: {player_2_score}")
        print(f"{player_1_name if player_1_score > player_2_score else player_2_name} wins.")