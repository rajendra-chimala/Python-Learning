age = int(input("Enter your age : "))



if((age <=0) and (age >=120 )):
    print("Invalid Age !")
elif(age<=18):
    print("You are under Age !")
else:
    print("You are eligible for vote !")