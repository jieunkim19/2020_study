# 변수 선언
ex_dict= {
    "키A" : "값A",
    "키A" : "값B",
    "키A" : "값C",
}

# 딕셔너리의 items() 함수 결과 출력
print("# 딕셔너리의 items() 함수")
print("items(): ", ex_dict.items())
print()

# for 반복문과 items() 함수 조합해서 사용
print("# 딕셔너리의 items() 함수와 반복문 보합")

for key, element in ex_dict.items():
    print("dictionary[{}] = {}".format(key, element))
