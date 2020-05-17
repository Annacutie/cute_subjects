from random import randint

def speed_and_time(s, t):
    return s*t

def gen_phisics_test():
    b=[]
    for i in range(12):
        s=randint(2, 12)
        t=randint(2, 12)
        b.append((f"time: {s} min speed: {t} cm/sec", speed_and_time(s, t)))

    return b
