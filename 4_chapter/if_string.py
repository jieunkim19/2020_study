# 변수 선언
number = int(input("정수 입력> "))

# if 조건문으로 홀수, 짝수 구분
if number % 2 == 0:
    print("""\
        입력한 문자열은 {}입니다.
        {}은 짝수.""".format(number, number))
else:
    print("""\
        입력한 문자열은 {}입니다.
        {}은 홀수.""".format(number, number))
