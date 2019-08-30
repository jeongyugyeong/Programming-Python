class car:
    count = 0 #클래스 변수

    @classmethod
    def get_count(cls): #클래스 함수
        return cls.count

    def __init__(self, type, speed):
        self.type = type
        self.speed = speed
        car.count += 1

    def move(self):
        print(self.type + "가 " + str(self.speed) + " 속도로 움직입니다.")

    def speed_up(self, amount):
        self.speed += amount

    def speed_down(self, amount):
        self.speed -= amount

print(car.get_count())
c1 = car("스포츠카", 100) #count 변수를 얘네들이 공유하고 있음(객체 간에 공유할 게 있으면 class로)
c2 = car("트럭", 50)
c3 = car("벤츠", 300)
print(car.get_count())
