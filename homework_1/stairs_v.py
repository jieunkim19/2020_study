# 1) for

#for i in range(1, 6): # * 반복
#    for j in range(6-i): # 공백 반복
#        print(" ", end="")
#    for j in range(i):
#        print("*", end="")
#    print()


# 2) format
# format{:>5}, 맨 오른쪽에 별 출력, 나머지는 공백 출력

for i in range(5):
    print("{:>5}".format("*" * (i +1)))
