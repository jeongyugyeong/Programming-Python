def p( *args ):
    str = ""
    for a in args:
        str = str + a
    print(str)
p("♡")
p("♡", "♪")
p("♡", "♪", "♣", "♠")

def p( space, space_num, *args ):
    str = args[0]
    for i in range(1, len(args)):
        str = str + (space * space_num) + args[i]
    print(str)

p(",", 3, "♡", "♪")
p("☆", 2, "♡", "♪", "♣")
p("_", 3, "♡", "♪", "♣", "♠")

def p( space, space_num, *args ):
    string = args[0]
    for i in range(1, len(args)):
        string += (space * space_num) + args[i]
    print(string)

p(",", 3, "핱") #핱
p(",", 3, "핱")
p("별", 2, "핱", "음", "슾") #핱별별음별별슾

#p115 혼자해보기
def star():

star("음", 3)
#음음음

star("핱"), 1, 2, 3)
#핱
#핱핱
#핱핱핱

#star 함수 정의
def star(mark, repeat, space, space_repeat, line):
    for i in range(1, line):
        str = (mark * repeat)
        for j in range(2, repeat):
            str = str + (space * space_repeat) + (mark * repeat)
        print(string)

star("*", 2, "+", 3, 5)
print("--------------------")
star(mark="*", repeat=2, space="+", space_repeat=3, line=5)

def star2(mark, repeat, space, space_repeat, line):
    string = (mark*repeat)+(space*space_repeat)+(mark*repeat)
    for n in range(line):
        print(string)


star2("X", 3, "_", )

def hello2(name="무명", msg="안녕하세요"):
    print(name + "님, " + msg + "!")

hello("김철수", "오랜만이에요")
hello()

def fn(a, b=[]):
    b.append(a)
    print(b)

fn(3)
fn(5)
fn(10)

def hello(name, msg="안녕하세요", feeling="♡"):
    print(name + "님, " + msg + feeling)

hello("아무개")
hello("김철수", "오랜만이에요", "♬")

def gugudan(dan):
    pass

gugudan(3) #3단 출력
gugudan()

