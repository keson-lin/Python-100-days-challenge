# if/else
# 要求1:高於120CM
# 要求2:年齡小於12；5元，12~18；7元，以上12元
# 拍照加3元
# 中年危機 45~55歲免費
print("Welcome to the rollercaster!")
height = int(input("What is your height in cm? :"))

if height >= 120:
    age = int(input("What is your age?:"))
    if age<12:
        bill = 5
        print("Child ticket are 5$")
    elif age <= 18:
        bill = 7
        print("Youth ticket are 7$")
    elif age >=45 & age <=55:
        print("everything is OK. Have ride on us!!")
        bill = 0
    else:
        bill = 12
        print("Adult ticket are 12$")
    
    photo=input("Do you want a photo? Y or N.")
    if photo == "Y" or "y":
        bill += 3
    print(f"your bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")