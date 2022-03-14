from math import ceil,floor
count = 0
num1 = int(25317)
num2 = int(51237)
def is_prime(x):
    for i in range(2,ceil(x**0.5)+1):
        if x%i == 0:
            return False
    return True
def divisors(x):
    divs=[1,x]
    if x ** 0.5 == int(x**0.5):
        divs.append(int(x**0.5))
    for i in range(2,ceil(x**0.5)):
        if x%i == 0:
            divs.append(i)
            divs.append(x//i)
    return sorted(divs)
for i in range(num1,num2):
    d = divisors(i)
    if len(d)>=8:
        for j in range(len(d)):
            ans = is_prime(d[j])
            if ans == True:
                count+=1
        if count>=7:
            print(d)
