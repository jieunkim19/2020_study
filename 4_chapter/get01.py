# 딕셔너리 선언
dictionary = {
    "name" : "아엠 아이언맨",
    "who" : "유알 아이언맨"
    }

# 존재하지 않는 키에 접근
value = dictionary.get("존재하지 않는 키")
print("값: ", value)

# None 확인 방법
if value == None:
    print("존재하지 않는 키에 접근했었따.")
    
