#bit.ly/2UGlypH
#학번을 입력받고, 학년 학과 반 번호를 출력하자
#ex) 2520을 입력하면 2학년 뉴미디어디자인과 5반 20번입니다.

myNumber = input("학번을 입력해주세요 : ")

if myNumber[0] == 3:
    if myNumber[1] == "1" or myNumber[1] == "2":
        major = "인터랙티브미디어과"
    elif myNumber[1] == "3" or myNumber[1] == "4":
        major = "디자인과"
    else:
        major = "솔루션과"
else:
    if myNumber[1] == "1" or myNumber[1] == "2":
        major = "뉴미디어소프트웨어과"
    elif myNumber[1] == "3" or myNumber[1] == "4":
        major = "뉴미디어솔루션과"
    else:
        major = "뉴미디어디자인과"
        