try:
    file = open("info.txt","w")
    file.close()
except exception as e:
    print(e)

print("#파일 닫혔는지 확인해!")
print("file.closed:", file.closed)
