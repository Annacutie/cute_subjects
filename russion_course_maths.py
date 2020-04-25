from random import randint

operations=["+", "-", "*", "/", "**2", "**3"]

division_1=["12", "24", "36", "48", "60", "72", "84"]
division_2=["3", "4", "6", "12"]

def caluclate(p):
    '''
    this function takes a string problem and solves it
    returns answer as a number.

    >>> caluclate(["2", "+", "2"])
    4
    '''
    a=int(p[0])
    sighn=p[1]
    b=int(p[2])
    if sighn=="+":
        return a+b
    elif sighn=="x":
        return a*b
    elif sighn=="**":
        if b==2:
            return a**2
        elif b==3:
            return a**3
    elif sighn==":":
        return a//b
    elif sighn=="-":
        return a-b

def gen_answers(pr):
    '''
    This function uses caluclate as a tool to make
    answer list from question list
    >>>gen_answers([2+1, 3+6])
     [3, 9]
    '''
    a=[]
    for f in pr:
        problem=f.split(" ")
        aw=caluclate(problem)
        a.append(aw)
    return a

def gen_questions(number_of_questions, sign):
    '''
    This function makes the question list
    >>>gen_questions(3, +)
    ["345 + 342", "987+  908", "450 + 129"]
    '''
    maths=[]
    for i in (range(number_of_questions)):
        #maths=["12 + 34", "190 - 35", "45 + 8", "34 + 56", "90 + 89", "123 + 23"]
        if sign=="+":
            maths.append(f"{randint(100, 999)} + {randint(100, 999)}")
        elif sign=="*":
            maths.append(f"{randint(1, 9)} x {randint(1, 9)}")
        elif sign=="**2":
            maths.append(f"{randint(1, 10)} ** 2")
        elif sign=="**3":
            maths.append(f"{randint(1, 10)} ** 3")
        elif sign=="/":
             maths.append(f"{division_1[randint(0, 6)]} : {division_2[randint(0, 3)]}")
        elif sign=="-":
            maths.append(f"{randint(151, 999)} - {randint(100, 150)}")
    return maths


def gen_1_operation_test(s):
    '''
    this function defins an operation
    and biuld the work sheet using gen_questions
    for help
    >>>gen_1_operation_test(*)
    [3*8, 7*3, 9*7]
    '''
    if s in operations:
        return gen_questions(question_number, s)
    else:
        return gen_questions(question_number)
        '''
print("**2 это квадрат а куб это **3")
cute=input("Введите знак (+, -, /, **2, **3 или *): ")
print("")
question_number=int(input("Введите количество вопросов: "))
print("")
print("_"*19)
maths=gen_1_operation_test(cute)
#maths=gen_questions(question_number)
answers=gen_answers(maths)
'''
skore=0
def maths_lesson():
    '''
    this function diplays the worksheet
    and marks the answers
    >>>maths_lesson()
    2**2=4
    4**2=8
    '''
    for math in range(len(maths)):
        print("")
        print(f"{maths[math]} = ")
        n_1=input("Ваш ответ: ")
        try:
            n_1=int(n_1)
        except:
            n_1=None

    if n_1==answers[math]:
        print("правильно")
        skore=skore+1
    else:
        print("неправильно")
    return skore

def pesentege(s, g):
    return s/g*100

def check(correct_answers, user_answers, test_type="maths"):
    score=0

    for i in range(len(user_answers)):
        print(len(user_answers))
        try:
            if str(correct_answers[i]) == user_answers[f"q_{i}"]:
                score=score+1
        except:
            if correct_answer[i] == user_answers[f"q_{i}"]:
                score=score+1
    return score



def see_skore(s, g):
    '''
    This function
    gives grades
    >>>see_skore(4, 4)
    5
    '''
    if s==g:
        print("5")
    elif s==g-1:
        print("4")
    elif s==g-2:
        print("3")
    else:
        print("2")
