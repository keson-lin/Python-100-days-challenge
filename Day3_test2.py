#閏年計算
#要求:每4年一次閏年，不可以被100整除，可被400整除

age = int(input("please input age number:"))

if age % 4 == 0 :
    if age % 100 == 0:
        if age % 400 == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")