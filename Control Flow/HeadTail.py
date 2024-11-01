import random

def HeadTail():
    toss = random.randint(0, 1)
    print(f"Toss values is: {toss}")
    if toss == 0:
        return "Head"
    else:
        return "Tail"


result = HeadTail()
print(f"The result of the coin toss is: {result}")