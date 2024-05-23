import random

target = random.randint(1,100)



while True:
    userNum = (input("Guess the target number or Quit(Q):"))
    if(userNum == "Q"):
        break


    userNum = int(userNum)
    if(userNum == target):
        print("Success : Correct Guess!!")
        break
    elif(userNum < target):
        print("Your guess is too smaller.Take a bigger guess")
    else:
        print("Your guess is too bigger.Take a smaller guess")



print("----Game Over----")
    
     

    



