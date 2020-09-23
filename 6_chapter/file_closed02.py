try:
    file = open("info.txt","w")
    예외.발생해라()
    file.close()
except Exception as e:
    print(e)

print("#파일 닫혔는지 확인해!")
print("file.closed:", file.closed)
