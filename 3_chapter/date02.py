# 날짜, 시간 기능
import datetime

# 현재 날짜 구하는 함수
now = datetime.datetime.now()

# 오전
if now.hour < 12:
    print("{}시로 오전이당!!".format(now.hour))
# 오후
if now.hour > 12:
    print("{}시로 오후다...".format(now.hour))
