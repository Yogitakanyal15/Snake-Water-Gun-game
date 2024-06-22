import random

print("MENU")
print("1 for Snake\n2 for Water\n3 for Gun")

ch=1
while(ch==1):
    user=int(input("Enter your choice:"))
    computer=random.randint(1,3)     #random.choice([1,2,3])
    print("Computer's Choice is: ", computer)
    print("Your choice is: ",user)
    print("Result is: ")
    if(user==computer):
        print("It's tie!")
    elif(user==1 and computer==2):
        print("You win!")
    elif(user==1 and computer==3):
        print("You lose!") 
    elif(user==2 and computer==1):
        print("You lose!")
    elif(user==2 and computer==3):
        print("You lose!")
    elif(user==3 and computer==1):
        print("You win!")
    elif(user==3 and computer==2):
        print("You win!")
    else:
        print("You enetered a wrong choice!")
        
    ch=int(input("Do you want to enter more?(Y=1/N=0): "))

print("THANK YOU!!")