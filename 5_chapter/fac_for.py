def fac(n):

    #변수 선언
    output=1

    for i in range(1, n+1):
        output *= i

    return output

print("1!:", fac(1))
print("2!:", fac(2))
print("3!:", fac(3))
print("4!:", fac(4))
