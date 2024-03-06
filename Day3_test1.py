#BMI 2.0 加上 if/else 判斷


Weight=int(input("input your weight(KG):"))
Height=float(input("input your height(M):"))
BMI=Weight/Height**2
if BMI < 18.5 :
    print(f"you BMI is {BMI}, you are under weight")
elif BMI < 25 :
    print(f"you BMI is {BMI}, you are normal weight")
else:
    print(f"you BMI is {BMI}, you are over weight")