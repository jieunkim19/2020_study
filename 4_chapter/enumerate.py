# 변수 선언
list_a = ["모던", "패밀리"]

# 그냥 출력~!
print("# 단순 출력..우..")
print("list_a")
print()

# enumerate() 함수를 적용해 출력
print("# enumerate() 함수 적용")
print(enumerate(list_a))
print()

# list() 함수로 강제 변환
print("# list() 함수로 강제 변환")
print(list(enumerate(list_a)))
print()

# for 반복문과 enumerate() 함수 조합해서 사용
print("# 반복문과 조합하기")
for i, value in enumerate(list_a):
    print("{}번째 요소는 {}입니다.".format(i, value))
    
