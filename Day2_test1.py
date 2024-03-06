# BMI 計算器
#公式: BMI= 體重(KG)/身高**2(M**2)

Kg=input("input your weight(KG):")
Height=input("input your height(M):")
int_weight=int(Kg)
float_height=float(Height)
BMI=int_weight/float_height**2
print("your BMI IS:"+ str(BMI))