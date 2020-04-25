def comments(score):
    if score==10:
        return "Exallent!"
    elif score <=9 and score >=7:
        return "Good, Next time probobly error free."
    elif score <=6 and score >5:
        return "not very good."
    else:
        return "Urfull!Try better and never copy."
