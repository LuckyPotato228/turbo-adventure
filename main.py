from math import ceil, floor


num1 = int(25317)
num2 = int(51237)


def is_prime(x):
    for i in range(2, ceil(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def divisors(x):
    divs = [1, x]
    if x ** 0.5 == int(x ** 0.5):
        divs.append(int(x ** 0.5))
    for i in range(2, ceil(x ** 0.5)):
        if x % i == 0:
            divs.append(i)
            divs.append(x // i)
    return sorted(divs)


def eratosphenes(upto):
    upto += 1
    cand = list(range(upto))
    for seed in range(2, ceil(upto ** 0.5) + 1):
        if cand[seed] != 0:
            for i in range(seed * seed, upto, seed):
                cand[i] = 0
    primes = [i for i in cand if i > 1]
    return primes


def sum_of_num(x):
    num = int(x)
    sum = 0
    while (num != 0):
        sum = sum + num % 10
        num = num // 10
    return sum


def algorythm_1(x,y,z):
    a = list(eratosphenes(y))
    for i in range(len(a)):
        if x < a[i] < y and sum_of_num(a[i]) > z:
            print(a[i])

def algorythm_2(num1,num2):
    for i in range(num1,num2):
        count = 0
        d = divisors(i)
        if len(d)>=8:
            for j in range(len(d)):
                ans = is_prime(d[j])
                if ans == True:
                    count+=1
            if count>=6:
                print(i,d)
algorythm_2(25317,51237)