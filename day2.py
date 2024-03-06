#Data Types

#String
"hello"[0]

a="123"
b="456"
#Integer
123+456

123_456_789
#Float
pi=3.1415926

#Boolean

True
False

num_char = len(input("What's your name:"))
#print("your name has"+num_char+" charactors.")

#type function
print(type(num_char))

#change to string
New_num_char=str(num_char)
print(New_num_char)

#change to integer
print(int(a)+int(b))

print(eval(a)+eval(b))

#加減乘除
1+2
2-1
2*2
4/2
2**2

#4捨5入，(，)表示到小數點後幾位
round(9/4 ,2)

#去除小數點
10 // 3

#f-string加入變數

score = 0
height = 1.8
isWinning = True

print(f"yourscore is {score}, your height is {height},you are winning is {isWinning}")