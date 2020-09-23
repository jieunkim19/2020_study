#메모 변수 만들기

dictionary = {
    1: 1,
    2: 2
    }

#함수 선언
def fibonacci(n):
    if n in dictionary:

        #메모가 되었다면 메모된 값을 리턴
        return dictionary[n]
    else:
        output = fibonacci(n-1) + fibonacci(n-2)
        dictionary[n] = output
        return output

print("fibonacci(10):", fibonacci(10))
print("fibonacci(20):", fibonacci(20))
print("fibonacci(30):", fibonacci(30))
print("fibonacci(40):", fibonacci(40))
