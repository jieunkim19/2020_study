#입력 받기
x = input("정수 입력>")

#마지막 자리 숫자 추출
last_character = x[-1]


# 짝수(문자열 연산으로..)
if last_character in "02468":
    print("짝수")

# 홀수
if last_character in "13579":
    print("홀수")
          
   
