def test():
    print("test() 함수의 첫 줄")
    try:
        print("try 구문이 실행됨")
        return
        print("try 구문의 return 키워드 뒤")
    except:
        print("except 구문 실행됨")
    else:
        print("else 구문 실행됨")
    finally:
        print("finally 구문 실행됨")
    print("test() 함수의 마지막 줄")

test()
