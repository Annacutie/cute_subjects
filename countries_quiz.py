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

    def load_data(self):
        "this method takes information from the json file as it actioly was and returns it. Example:quiz.load_data() gives {qeastion: Where? , answer:there}"
        with open(self.data_file) as file:
            quiz_data=load(file)

        return quiz_data

    def gen_question(self, country, city_index):
        """makes a quetion."""
        return f"Where is {self.test_data[country]['cities'][city_index]} ?"

    def gen_options(self, correct_answer):
        options=[correct_answer, ]
        counter=0
        while counter < 2:
            option=self.test_data[choice(list(self.test_data.keys()))]['country']
            if option != correct_answer:
                options.append(option)
                counter=counter+1
            else:
                continue

        return options

#fiter options for same ones use cotine

    def gen_quiz(self):
        quiz=[]
        for key, value in self.test_data.items():
            question=self.gen_question(key, randint(0, 2))
            options=self.gen_options(value ['country'])
            correct_answer=value ['country']
            quiz.append({'question':question, 'options':options, 'correct answer':correct_answer})
        return quiz


#print 2 questions

#raserch for random functions find useful funktions copy paste of information and wright funktion list
'''
choices:
Return a k sized list of elements chosen from the population with replacement. If the population is empty, raises IndexError.

choice:
Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError.
'''

#comment the class and methods
