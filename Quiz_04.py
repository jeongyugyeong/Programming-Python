#주차요금 계산
import sys

print("몇 분 주차하시겠습니까?")
time = int(input())
fee = 2000
if time <= 30 :
    fee=2000
elif time > 1440:
    print("24시간을 넘을 수 없습니다.")
    sys.exit()
else:
    time = time - 30
    fee=fee+(time//10)*1000
    if time%10!=0 : 
        fee=fee+1000

print("{}원".format(fee))
