l = [1, 2, 3]
try:
    print(1[2])
    print(1[3])     #IndexError
except IndexError:
    print("리스트의 요소에 접근하지 못했습니다.")
