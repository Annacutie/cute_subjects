from random import randint

def speed_and_time(s, t):
    return s*t

def gen_phisics_test():
    b=[]
    for i in range(10):
        s=randint(2, 12)
        t=randint(2, 12)
        b.append((f"время: {s} min скоросьть: {t} cm/sec", speed_and_time(s, t)))

    return b
