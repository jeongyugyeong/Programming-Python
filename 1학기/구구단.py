for dan in range(2, 9+1): #단
    for i in range(1, 9+1): #곱하기 1부터 9까지
        if i > 7:
            break
        if i % 2 == 0:
            continue
        print("{} x {} = {}".format(dan, i, dan*i))
    print("-----------")

array = []
for i in range(1, 10, 2):
    array.append(i)
print(array)

array2 = [i for i in range(1, 10, 2)]
print(array2)

array3 = [i*i for i in range(1, 10, 2)]
print(array3)

array4 = [i*i for i in range(1, 10, 2) if i*i > 30]
print(array4)

array5 = [] #list comprehension 풀면 이렇게
for i in range(i, 10, 2):
    if i*i > 30:
      array5.append(i*i)
print(array5)
