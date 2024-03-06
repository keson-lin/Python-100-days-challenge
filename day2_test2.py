#計算一個人活到90歲還有多少時間

ages = input("please input your age:")

years = 90 - int(ages)

months = years * 12
weeks = years * 52
days = years * 365 

print(f"you have {years} years left, and {months} months left, and {weeks} weeks left, and {days} days left")