# 딕셔너리 선언
dictionary = {
    "name" : "망고..",
    "type" : "설탕에 절인..(엄청 달겠당)",
    "ingredient" : ["맹고", "슈가", "뭔나트륨", "뭔색소"],
    "origin" : "우리집"
    }

# 출력
print("name:", dictionary["name"])
print("type: ", dictionary["type"])
print("ingredient: ", dictionary["ingredient"])
print("origin: ", dictionary["origin"])
print()

# 값 변경
dictionary["name"] = "망고가 아닌 딸긔!"
print("name: ", dictionary["name"])
