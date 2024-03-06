# 小費計算器
# 要求: 小費級距 10%,12%,15%，幾個人分攤 ，精確到小數點2位
print("Welcome to the tip calculator.")
total = float(input("What was the total bill? :"))
range = int(input("What percentage tip would you like to give? 10%,12%,15% :"))
people = int(input("How many people to split the bill :"))
tips = (range / 100 * total + total) / people
print(f"Each person should pay :{tips}")