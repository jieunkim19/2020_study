print("start")
while True:
    try:
        print("try 구문 실행됨")
        break
        print("try 구문 break 키워드 뒤")
    except:
        print("except 구문 실행됨")
    finally:
        print("finally 구문 실행됨")
    print("while 반복문 마지막 줄")
print("프로그램 종료")
