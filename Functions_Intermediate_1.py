import random
def randInt(min=0,max=101):
    if max<min:
        return False
    elif max < 0:
        return False
    else:
        num = random.randrange(min,max)
        return num
print(randInt())
print(randInt(100,1))
print(randInt(-4,-1))