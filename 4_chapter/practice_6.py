# 딕셔너리의 리스트 선언
pets = [
    {"name":"구름", "age":5},
    {"name":"초코", "age":3},
    {"name":"아지", "age":1},
    {"name":"랑이", "age":1}
    ]

for pet in pets:
    print(pet["name"], str(pet["age"])+"살")
