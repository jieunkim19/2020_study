list_input=["52", "273", "32", "t", "103"]

list_number=[]
for item in list_input:

    try:
        float(item)
        list_number.append(item)
    except:
        pass

print("{}내부에 잇는 숫자는".format(list_input))
print("{}다".format(list_number))
