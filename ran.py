import random
m = random.randint(1,20)
a = int(input("Guess the number:\n"))
c = 100
for i in range(5):
    if (a==m):
        print("Hurray!!!")
        break
    else:

        b=(m-a)
        if(b>=10 ):
            print("too low")
        elif(b<= -10):
            print("too high")
        elif ((b <= -5) and (b> -10)):
            print("high")
        elif ((b >= 5) and (b<10)):
            print("low")
        elif ((b < 5) and (b>0)):
            print("not low")
        elif ((b > -5) and (b<0)):
            print("not high")
        a=int(input("Enter again::\n"))
    c-=20
print(f"Your score is {c}")
print(f"{m} is correct!!!")
