


print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L")  
add_pepperoni = input("Do you want pepperoni? Y or N") 
extra_cheese = input(" Do you want extra cheese? Y or N") 

bill = 0

if size == "L":
  bill += 25
if size == "M":
  bill += 20
if size == "S":
  bill += 15
else : print("please input again")

if add_pepperoni == "Y":
  if size =="L":
    bill +=3
else:
  bill+=2

if extra_cheese == "Y":
  bill+= 1

print(f"your pizza total bill is ${bill}")