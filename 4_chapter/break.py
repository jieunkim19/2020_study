# 변수 선언
i = 0

# 무한 반복
while True:
    print("{}번째 반복중이다.".format(i))
    i = i+1

    # 반복 종료
    input_text = input(">종료할랭?(y): ")
    if input_text in["y", "Y"]:
        print("반복 종료")
        break
