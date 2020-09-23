# 딕셔너리 선언
dictionary = {
    "name" : "아엠 아이언맨",
    "who" : "유알 아이언맨"
    }

# 요소 삭제 전에 내용 출력
print("요소 삭제 전: ", dictionary)

# 요소 삭제
del dictionary["name"]
del dictionary["who"]

# 출력
print("요소 삭제 후: ", dictionary)
