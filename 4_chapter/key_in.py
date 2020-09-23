# 딕셔너리 선언
dictionary = {
    "name" : "아엠 아이언맨",
    "who" : "유알 아이언맨"
    }

# 입력 받기
key = input(">접근하고자 하는 키: ")

# 출력
if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 키에 접근 중")

    
