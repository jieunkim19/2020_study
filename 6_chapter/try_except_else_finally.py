try:
    number_input=int(input("정수 입력>"))

    print("반지름", number_input)
except:
    print("정수 입력하시오")
else:
    print("예외가 발생하지 않음")
finally:
    print("일단 프로그램 종료하겠다")
