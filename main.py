from math import ceil, floor
def is_prime(x):
    for i in range(2,ceil(x**0.5)+1):
        if x % i == 0:
            return False
        return True
count = 0
first = int (input())
second = int(input())
Luke = [3,2]
for i in range(2,1000):
    if Luke[i-1]+Luke[i-2] > second:
        break
    Luke+= [Luke[i-1]+ Luke[i-2]]

for j in range(len(Luke)):
    if Luke[j]>first and Luke[j]<second and is_prime(Luke[j])== True:
            print(j+1)
            print(Luke[j])
            count+=1
print(count)
print(*Luke)