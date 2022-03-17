from math import ceil, floor


def is_prime(x):
    if x != 2:
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
        prime_nums = []
        count = 0
        d = divisors(i)
        if len(d)>=8:
            for j in range(len(d)):
                ans = is_prime(d[j])
                if ans == True:
                    prime_nums += [d[j]]
                    count+=1
            if count>=7:
                print(i,d)
                print(prime_nums)


def algorythm_3(num1,num2,step):
    for i in range(num1,num2):
        d = divisors(i)
        count = 0
        for j in range(len(d)-1):
            if j>1:
                if d[j] == d[j-1]+step:
                    count+=1
            if len(d) > 3 and count == len(d)-2:
                print(i)
                print(d)


def algorythm_4():
    pass


def algorythm_5():
    pass


algorythm_3(854321,1087654,10)
