#get data
#generate QUESTIONS
#gen 3 answer options
#check answer
from json import *
from random import *


class Quiz(object):
    """This class makes a quiz"""

    def __init__(self, data_file):
        "this is the mian function of the class"
        self.data_file = data_file
        self.test_data = self.load_data()
        self.correct_answers=[]

    def load_data(self):
        "this method takes information from the json file as it actioly was and returns it. Example:quiz.load_data() gives {qeastion: Where? , answer:there}"
        with open(self.data_file) as file:
            quiz_data=load(file)

        return quiz_data

    def gen_question(self, rand_index):
        """makes a quetion."""
        return f" {self.test_data[rand_index]['word']}."

    def gen_options(self, rand_index):
        options=[]
        options.append(self.test_data[rand_index]['definition'])
        counter=0
        while counter < 2:
            option=self.test_data[randint(0, 5999)]['definition']
            if option != options[0]:
                options.append(option)
                counter=counter+1
            else:
                continue
        shuffle(options)

        return options

#fiter options for same ones use cotine
    def get_correct_answers(self):
        return self.correct_answers

    def gen_quiz(self):
        quiz=[]

        for value in range(12):
            current_index=randint(0, 5999)
            question=self.gen_question(current_index)
            options=self.gen_options(current_index)
            correct_answer=self.test_data[current_index]['definition']
            self.correct_answers.append(correct_answer)
            quiz.append({'question':question, 'options':options, 'correct answer':correct_answer})
        return quiz

#print 2 questions
quiz = Quiz("sat_world_tour_data.json")
print(quiz)
#raserch for random functions find useful funktions copy paste of information and wright funktion list
'''
choices:
Return a k sized list of elements chosen from the population with replacement. If the population is empty, raises IndexError.

choice:
Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError.
'''

#comment the class and methods
