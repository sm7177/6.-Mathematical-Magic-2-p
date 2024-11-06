ten= 10
hun= 100

print("Prime numbers between", ten, "and", hun, "are:")

for num in range(ten,hun+1):
    
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)