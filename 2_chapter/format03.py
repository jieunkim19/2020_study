# 기호와 함께 출력
output_f= "{:+d}".format(52) # {+d}처럼 앞에 +기호를 추가하면 +기호 함께 출력
output_g= "{:-d}".format(52) # 음수
output_h= "{: d}".format(52) # 양수: 기호 부분 공백
output_i= "{: d}".format(-52) # 음수: 기호 부분 공백

print("# 기호와 함께 출력")
print(output_f)
print(output_g)
print(output_h)
print(output_i)
