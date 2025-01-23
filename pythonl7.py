import random
number=random.randint(1,9)
print(number)
if number<4:
    print("too low")
elif number==5:
    print("exactly right")   
else:
    print("too high")    