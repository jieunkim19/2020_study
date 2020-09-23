# 숫자는 무작위로 입력해도 상관 없음
numbers = [1, 2, 6, 8,2, 4 ,3, 8,5 ,6 , 7 , 8 ,9 ,1, 3, 5]
counter = {}

for number in numbers:
    if number in counter:
        counter[number]=counter[number]+1
    else:
        counter[number]=1

print(counter)
