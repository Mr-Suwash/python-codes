import random
m = random.randint(1,20)
a = int(input("Guess the number:\n"))
c = 6
for i in range(5):
    c-=1
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
if(c==5):
    print(f"Your score is 25")
elif(c==4):
    print(f"Your score is 20")
elif(c==3):
    print(f"Your score is 15")
elif(c==2):
    print(f"Your score is 10")
elif(c==1):
    print(f"Your score is 5")
else:
    print(f"Your score is 0")
print(f"{m} is correct!!!")