# 날짜, 시간 기능
import datetime

# 현재 날짜 구하는 함수
now = datetime.datetime.now()

print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
    ))
