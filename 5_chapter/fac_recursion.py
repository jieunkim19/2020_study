def fac(n):
    if n == 0:
        return 1
    else: 
        return n * fac(n-1)

#함수 호출
    print("1!:", fac(1))
    print("2!:", fac(2))
    print("3!:", fac(3))
