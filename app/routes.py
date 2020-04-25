from app import app, db
from flask import render_template, request, session, url_for, redirect
from russion_course_maths import gen_questions
from russion_course_maths import gen_answers, check, pesentege
from random import randint
from pysics import *
from helpers import *
from comments import *
from app.forms import DeleteForm, LoginForm, RegistrationForm, ChangePassword
from flask_login import current_user, login_user
from app.models import User, Progress, ResetPassword
from flask_login  import logout_user, login_required
from English_quiz import *
from sqlite3 import *

operations=["+", "-", "*", "/", "**2", "**3"]
@app.route("/")
@app.route("/index")
def index():
    title={"main_title":"Cute subjects"}
    maths_test={}
    maths_test["questions"]=gen_questions(10, operations[randint(0, 5)])
    return render_template("index.html", title=title, maths_test=maths_test)

@app.route("/maths/addtion/", methods=["GET", "POST"])
def maths_addition():
    info=load_json("addition", "Maths.json")
    maths_test={}
    maths_test["questions"]=gen_questions(10, "+")
    maths_test["correct_answers"]=gen_answers(maths_test["questions"])
    session["correct_answers"]=maths_test["correct_answers"]
    maths_test["score"]=0
    session["test_type"]="maths"
    return render_template("maths.html", info=info, maths_test=maths_test)

@app.route("/maths/multiplication/")
def maths_multiplication():
    info=load_json("multiplication", "Maths.json")
    maths_test={}
    maths_test["questions"]=gen_questions(10, "*")
    maths_test["correct_answers"]=gen_answers(maths_test["questions"])
    session["correct_answers"]=maths_test["correct_answers"]
    maths_test["score"]=0
    session["test_type"]="maths"
    return render_template("maths.html", info=info, maths_test=maths_test)

@app.route("/maths/division/")
def maths_division():
    info=load_json("division", "Maths.json")
    maths_test={}
    maths_test["questions"]=gen_questions(10, "/")
    maths_test["correct_answers"]=gen_answers(maths_test["questions"])
    session["correct_answers"]=maths_test["correct_answers"]
    maths_test["score"]=0
    session["test_type"]="maths"
    return render_template("maths.html", info=info, maths_test=maths_test)

@app.route("/maths/exponents/")
def maths_exponents():
    info=load_json("exponents", "Maths.json")
    maths_test={}
    maths_test["questions"]=gen_questions(10, "**2")
    maths_test["correct_answers"]=gen_answers(maths_test["questions"])
    session["correct_answers"]=maths_test["correct_answers"]
    maths_test["score"]=0
    session["test_type"]="maths"
    return render_template("maths.html", info=info, maths_test=maths_test)
#two routes(substruction and cube) make
@app.route("/maths/cube/")
def maths_cube():
    info=load_json("cube", "Maths.json")
    maths_test={}
    maths_test["questions"]=gen_questions(10, "**3")
    maths_test["correct_answers"]=gen_answers(maths_test["questions"])
    session["correct_answers"]=maths_test["correct_answers"]
    maths_test["score"]=0
    session["test_type"]="maths"
    return render_template("maths.html", info=info, maths_test=maths_test)

@app.route("/maths/substruction/")
def maths_substruction():
    info=load_json("substruction", "Maths.json")
    maths_test={}
    maths_test["questions"]=gen_questions(10, "-")
    maths_test["correct_answers"]=gen_answers(maths_test["questions"])
    session["correct_answers"]=maths_test["correct_answers"]
    maths_test["score"]=0
    session["test_type"]="maths"
    return render_template("maths.html", info=info, maths_test=maths_test)

@app.route("/physics",  methods=["POST", "GET"])
def physics_problem():
    physics_test={}
    physics_test["test"]=gen_phisics_test()
    physics_test["title"]="Speed and time"
    physics_test["task"]="fill in the gaps"
    session["test_type"]="science"
    answers=[]
    for i in physics_test["test"]:
        answers.append(i[1])
    session["correct_answers"]=answers

    physics_test["score"]=0
    return render_template( "physics.html", physics_test=physics_test)

@app.route("/english/define_word", methods=["POST", "GET"])
def define_words_tests():
    info={"title":"define words"}
    word_quiz=Quiz("sat_world_tour_data.json")
    quiz=word_quiz.gen_quiz()
    session["correct_answers"]=word_quiz.get_correct_answers()
    session["test_type"]="english"
    print(f"session['correct_answers']{session['correct_answers']}")
    return render_template("English.html", quiz=quiz, info=info)

@app.route("/check",  methods=["POST", ])
def result():
    user_answers=request.form
    answer_list=[]
    print(user_answers)
    '''
    for i in user_answers:
        try:
            answer=int(i)
            answer_list.append(answer)
        except:
            answer_list.append(i)
            '''
    if session["test_type"]=="english":
        score=check(session["correct_answers"], user_answers, "english")
        #print(f"this is user's answers {answer_list}")
    else:
        score=check(session["correct_answers"], user_answers)
    m=''
    if current_user.is_authenticated:
        c_user=Progress.query.filter_by(user_id=current_user.id).first()
        c_user.total_score=c_user.total_score + score
        if session["test_type"] == "maths":
            c_user.maths_score=c_user.maths_score + score
            db.session.commit()


        elif session["test_type"] == "science":
            c_user.science_score=c_user.science_score + score
            db.session.commit()
        elif session["test_type"] == "english":
            c_user.english_score=c_user.english_score + score
            db.session.commit()
    else:
        m="You need to login in order to save your score"
    reward_statmet=reward(score)
    print(f'This is correct answers {session["correct_answers"]}')
    #session.pop("correct_answers", None)
    comment=comments(score)
    #score=check(session["correct_answers2"], answer_list)
    pestege=pesentege(score, 10)
    #session.pop("correct_answers2")
    return render_template("check.html", result=score, comment=comment, pestege=pestege, reward_statmet=reward_statmet, m=m)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            return render_template("login.html", form=form)
        else:
            login_user(user, remember=form.remember_me.data)
            return render_template("index.html", title="Cute Subjects")
    return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/profile/<username>")
@login_required
def profile(username):
    user = User.query.filter_by(username = username).first_or_404()
    progress = Progress.query.filter_by(user_id=user.id).first()
    return render_template("profile.html", user=user, progress=progress)

@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form=RegistrationForm()
    if form.validate_on_submit():
        u=User(username=form.username.data, email=form.email.data)
        u.set_password(form.password.data)
        db.session.add(u)
        db.session.commit()
        score_data=Progress(total_score=0, maths_score=0, science_score=0, english_score=0, student=u)
        db.session.add(score_data)
        db.session.commit()
        secret_q_1=ResetPassword(question=request.form["secret_question_1"], answer=request.form["answer_1"], user_id=u.id)
        secret_q_2=ResetPassword(question=request.form["secret_question_2"], answer=request.form["answer_2"], user_id=u.id)
        db.session.add(secret_q_1)
        db.session.add(secret_q_2)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template("sign_up.html", form=form)

@app.route("/settings", methods=["GET", "POST"])
@login_required
def settings():
    check_q=ResetPassword.query.filter_by(user_id=current_user.id).all()
    print(check_q)
    if request.method=="POST":
        u=User.query.get(current_user.id)
        if 'delete_submit' in request.form.keys():
            if u.check_password(request.form["password"]):
                db.session.delete(u)
                db.session.commit()

        if 'change_submit' in request.form.keys():
            if u.check_password(request.form["old_password"]):
                u.set_password(request.form["new_password"])
                db.session.commit()
            return render_template("settings.html", message="Your password has been changed")

        if 'secret_submit' in request.form.keys():
            check_q=ResetPassword.query.filter_by(user_id=current_user.id).all()
            if check_q==[]:
                secret_q_1=ResetPassword(question=request.form["secret_question_1"], answer=request.form["answer_1"], user_id=current_user.id)
                secret_q_2=ResetPassword(question=request.form["secret_question_2"], answer=request.form["answer_2"], user_id=current_user.id)
                db.session.add(secret_q_1)
                db.session.add(secret_q_2)
                db.session.commit()

            else:
                check_q[0].question=request.form["secret_question_1"]
                check_q[0].answer=request.form["answer_1"]
                check_q[1].question=request.form["secret_question_2"]
                check_q[1].answer=request.form["answer_2"]
                db.session.commit()

    return render_template("settings.html")

@app.route("/reset_password", methods=["GET", "POST"])
def reset_password():
    username = request.args.get('username')
    u=User.query.filter_by(username=username).first()
    check_q=ResetPassword.query.filter_by(user_id=u.id).all()
    questions={"q1":check_q[0].question, "q2":check_q[1].question}
    if request.method=="POST":
        if 'secret_submit' in request.form.keys():

            if request.form["answer_1"].lower()==check_q[0].answer.lower() and request.form["answer_2"].lower()==check_q[1].answer.lower():
                u.set_password(request.form["new_password"])
                db.session.commit()
            elif request.form["answer_1"].lower()==check_q[1].answer.lower() and request.form["answer_2"].lower()==check_q[0].answer.lower():
                u.set_password(request.form["new_password"])
                db.session.commit()

        return render_template("Reset_password.html", questions=questions)
    return render_template("Reset_password.html", questions=questions)

@app.route("/get_reset", methods=["GET", "POST"])
def get_reset():
    if request.method=="POST":
        username=request.form['username']
        return redirect(url_for("reset_password", username=username))

    return render_template("user_name.html")
    #return redirect(url_for("reset_password", username=username))
