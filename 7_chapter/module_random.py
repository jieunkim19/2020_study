import random
print("# random 모듈")

# random(): 0.0 <= x < 1.0 사이의 float를 리턴합니다.
print("- random():", random.random())

#uniform(min, max): 지정한 범위 사이의 float를 리턴합니다.
print("- uniform(10, 20):", random.uniform(10, 20))

print("-randrange(10):", random.randrange(10))

print("-choice([1,2,3,4,5])", random.choice([1,2,3,4,5]))
