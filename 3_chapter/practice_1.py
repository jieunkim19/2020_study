#두 개 입력받아서 숫자 크기 비교
a = float(input("> 첫 번째 숫자: "))
b = float(input("> 두 번째 숫자: "))
print()

if a>b:
    print("처음 입력했던 {}가 {}보다 더 크다".format(a, b))

if a<b:
    print("두 번쨰로 입력했던 {}가 {}보다 더 크다".format(b, a))

