#369게임

for i in range(1, 99+1):
    if i<10 and i%3==0:
        print('짝')
    elif 10<=i and (i//10==3 or i//10==6 or i//10==9): #십의 자리가 3, 6, 9인지
        print('짝')
    elif 10<=i and (str(i)[1]=='3' or str(i)[1]=='6' or str(i)[1]=='9'): #일의 자리가 3, 6, 9인지
        print('짝')
    else:
        print(i)
