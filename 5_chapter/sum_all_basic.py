#함수 선언

def sum_all(start, end):

    #변수 선언
    output = 0

    #반복문을 돌려 숫자를 더함
    for i in range(start, end +1):
        output +=i

    #리턴
    return output

print("0 tp 100:", sum_all(0, 100))
print("0 tp 1000:", sum_all(0, 1000))
print("50 tp 100:", sum_all(50, 100))
print("500 tp 1000:", sum_all(500, 1000))
