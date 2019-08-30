#숫자를 입력받아 각 자릿수의 합을 구하는 게임
#331을 입력하면, 7 출력
#10을 입력하면, 1 출력

echo = input("숫자를 입력해주세요")
total=0
for i in range (0,len(echo) ):
    total+=int(echo[i])
print("두 수의 합은 %s 입니다" % total)
