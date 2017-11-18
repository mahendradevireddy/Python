import random

playerhp = 240
attackl = 60
attackh = 80

while playerhp > 0:
    tmp = random.randrange(attackl, attackh)
    playerhp = playerhp - tmp

    if playerhp <= 0:
        playerhp = 0

    print("playerhp:",playerhp ,"for attack",tmp)