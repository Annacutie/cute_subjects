from random import randint

operations=["+", "-", "*", "/", "**2", "**3"]

division_1=["12", "24", "36", "48", "60", "72", "84"]
division_2=["3", "4", "6", "12"]

def caluclate_doble(p):
    '''
    this function takes a string problem and solves it
    returns answer as a number.

    >>> caluclate(["2", "+", "2", "-", "3"])
    1
    '''
    a=int(p[0])
    sighn_1=p[1]
    b=int(p[2])
    sighn_2=p[1]
    c=int(p[2])
    if sighn_1=="+" and sighn_2=="-":
        return a+b-c
    elif sighn_1=="-" and sighn_2=="+":
        return a-b+c

def gen_answers_2(pr):
    '''
    This function uses caluclate as a tool to make
    answer list from question list
    >>>gen_answers([2+1, 3+6])
     [3, 9]
    '''
    a=[]
    for f in pr:
        problem=f.split(" ")
        aw=caluclate_triple(problem)
        a.append(aw)
    return a

def gen_doble_questions(number_of_questions, sign_1, sign_2):
    '''
    This function makes the question list
    >>>gen_questions(3, +)
    ["345 + 342-200", "987 + 908 - 500", "450 + 129 - 100"]
    '''
    maths=[]
    for i in (range(number_of_questions)):
        if sign_1=="+" and sign_2=="-":
            maths.append(f"{randint(100, 999)} + {randint(100, 999)} - {randint(100, 500)}")

        if sign_1=="-" and sign_2=="+":
            maths.append(f"{randint(100, 999)} - {randint(100, 999)} + {randint(100, 500)}")

    return maths


def gen_2_operation_test(s):
    '''
    this function defins an operation
    and biuld the work sheet using gen_questions
    for help
    >>>gen_1_operation_test(*)
    [3*8, 7*3, 9*7]
    '''
    if s in operations:
        return gen_doble_questions(question_number, s)
    else:
        return gen_doble_questions(question_number)
