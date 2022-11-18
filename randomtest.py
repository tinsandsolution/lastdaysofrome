import random

random.seed(1)
random.seed(random.randint(1,100))

def nd6(n):
    return [random.choice([1,2,3,4,5,6]) for i in range(n)]

print(nd6(3))
print(nd6(3))
print(nd6(3))
print(nd6(3))
print(nd6(3))
print(nd6(3))
