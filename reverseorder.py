number= int(input("What is your number? "))
sum = 0
while number>0:
    number = number // 10
    sum = sum + 1
print(sum)
