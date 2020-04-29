from json import *
from random import randint
def load_json(key, json_file):
    with open(json_file) as file:
        data=load(file)
        info=data[key]

    return info
#fix ather routes
def super_int(var):
    try:
        new_var=int(var)
    except:
        new_var=ord(var)

    return new_var
'''
def reward(score):
    video_id=load_json(randint(0, 3), "muvies.json")
    video_name=video_id["name"]
    if score>8:
        return [video_id, video_name]
    else:
        return ["If your score is more then 8/10 you will get a moivie", ]
'''
