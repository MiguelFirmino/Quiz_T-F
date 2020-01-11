import random
from Quiz_Questions import game_questions

questions = [*game_questions]
def game():
    print('-' * 20)
    player_score = 0
    right_answers = 0
    wrong_answers = 0
    while len(questions) > 0:
        question = random.choice(questions)
        questions.remove(question)
        print(question.text)
        user_answer = input('Insert answer (Yes or No): ')
        while user_answer not in ['yes', 'y', 'f', 'true', 'no', 'n', 'f', 'false']:
            print('Sorry, that is an invalid answer')
            user_answer = input('Please insert another answer (Yes or No): ')
        if user_answer.lower() in question.correct_answer:
            player_score += question.question_reward
            right_answers += 1
            print('You got it right! (+{} points)'.format(question.question_reward))
            print('You have {} points'.format(player_score))
        else:
            wrong_answers += 1
            print('You got it wrong, good luck next time!')
        print('-' * 20)
    print('Congratulations! You have answered all the questions!')
    print('Your final score is {} points'.format(player_score))
    print('You answered {} questions right'.format(right_answers))
    print('And {} questions wrong.'.format(wrong_answers))
game()