table = [
    ["월", "화", "수"], #첫째 단(row)
    [1, 2, 3] #둘째 단(row)
]
for row in table: #출력문
  for col in row: #한 단에 하나씩
      print(col)
  print("------") #for문 안에 for문이 있고 그게 다 끝나면 이 줄 실행함
 