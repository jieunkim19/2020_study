limit = 10000
i = 1

sum_value = 0

while sum_value < limit:
    sum_value += i
    i += 1

print("{}를 더할 때 {}을 넘으며 그떄의 값은{}이다.".format(i, limit, sum_value))