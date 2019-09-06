# 국어, 영어, 수학, 자바, 파이썬, JSP 점수 입력받기
# 총점, 평균 구하기
# 용돈 구하기
# 평균 90점 이상 10000원
# 평균 80점 이상 10000원
# 평균 70점 이상 10000원
# 평균 60점 이상 10000원
# 그 미만 50000원

k = input('국어 점수 : ')
e = input('영어 점수 : ')
m = input('수학 점수 : ')
j = input('자바 점수 : ')
p = input('파이썬 점수 : ')
js = input('JSP 점수 : ')
sum = int(k) + int(m) + int(e) + int(j) + int(p) + int(js)
print("총점은", sum)
avg = sum/6
print("평균은", round(avg,2))
if avg >= 90:
    print("용돈 : 100000원")
elif avg >= 80:
    print("용돈 : 80000원")
elif avg >= 70:
    print("용돈 : 70000원")
elif avg >= 60:
    print("용돈 : 60000원")
else:
    print("용돈 : 50000원")









