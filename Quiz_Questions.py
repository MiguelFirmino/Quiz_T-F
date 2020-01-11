class Question():
    def __init__(self, text, correct_answer, question_reward):
        self.text = text
        if correct_answer == 'True':
            self.correct_answer = ['yes', 'y', 'f', 'true']
        elif correct_answer == 'False':
            self.correct_answer = ['no', 'n', 'f', 'false']
        self.question_reward = question_reward
game_questions = [Question('Russia has a larger surface area than Pluto.', 'True', 7),
                  Question('There are as many stars in space than there are grains of sand on every beach in the world.', 'False', 5),
                  Question('For every human on Earth there are 1.6 million ants.', 'True', 8),
                  Question('On Jupiter and Saturn it rains diamonds.', 'True', 9),
                  Question('Scotland’s national animal is the phoenix.', 'False', 4),
                  Question('A banana is a berry.', 'True', 8),
                  Question('An octopus has three hearts.', 'True', 4),
                  Question('There are 10 times more bacteria in your body than actual body cells.', 'True', 9),
                  Question('Rhode Island is the closest US state to Africa.', 'False', 3),
                  Question('Shakespeare made up the name “Sarah” for his play Merchant of Venice.', 'False', 3)]