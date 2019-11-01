# 아마스빈 주문 앱
# Drink <- Coffee
#      <- BubbleTea
# Order
# 메뉴 보여주자
# 음료 주문하자
# 주문한 음료 보여주자
# 총 금액 계산하자

class Drink:
    _cups = ["레귤러", "점보"]  # 리스트. 앞의 밑줄을 쓰는 이유는 밖에서 접근하면 안되는 정보이기 때문.
    _ices = ["0%", "50%", "100%", "150%"]
    _sugars = ["0%", "50%", "100%", "150%"]

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.cup = 0  # 기본값으로 초기화
        self.ice = 2
        self.sugar = 2
        # 넣을 게 없으면 self.name = none 처럼 사용 가능

    def __str__(self):
        return "이름 : " + self.name + "\t가격 : " + str(self.price) + "원\t컵 사이즈 : " + Drink._cups[self.cup] \
               + "\t얼음량 : " + Drink._ices[self.ice] + "\t당도 : " + Drink._sugars[self.sugar]
        # 클래스 변수 / 멤버변수는 __init__에서 초기화 해줘야 함 !!!

    def set_cup(self):
        self.cup = input("컵 사이즈를 선택하세요 (0: 레귤러, 1: 점보) : ")
        if self.cup == "":  # 사용자가 엔터만 치면 기본값 0을 넣자
            self.cup = 0
        else:
            self.cup = int(self.cup)  # 혹시 정수형으로 선택하지 않을 경우에 대비

        # 점보 사이즈면 300원 추가
        if self.cup == 1:
            self.price += 300

    def set_ice(self):
        self.ice = input("얼음량을 선택하세요 (0: 0%, 1: 50%, 2: 100%, 3: 150%) : ")
        if self.ice == "":
            self.ice = 2
        else:
            self.ice = int(self.ice)

    def set_sugar(self):
        self.sugar = input("당도를 선택하세요 (0: 0%, 1: 50%, 2: 100%, 3: 150%) : ")
        if self.sugar == "":
            self.sugar = 2
        else:
            self.sugar = int(self.sugar)

    def order(self):
        # 파이썬은 자신의 함수를 호출할 때에도 앞에 self.을 붙여야 함
        self.set_cup()
        self.set_ice()
        self.set_sugar()


class Coffee(Drink):
    pass


class BubbleTea(Drink):
    _pearls = ["타피오카펄", "코코펄", "젤리펄", "알로에펄"]

    def __init__(self, name, price):
        super().__init__(name, price)  # Drink의 생성자 가져옴
        self.pearl = 0

    def __str__(self):
        return super().__str__() + "\t펄: " + BubbleTea._pearls[self.pearl]

    def set_Pearl(self):
        self.pearl = input("펄을 선택하세요 (0: 타피오카펄, 1: 코코펄, 2: 젤리펄, 3: 알로에펄) : ")
        if self.pearl == "":
            self.pearl = 0
        else:
            self.pearl = int(self.pearl)

    def order(self):
        super().order()  # Drink의 order()함수
        self.set_Pearl()


class Order:
    _menus = [Coffee("아메리카노", 1800), BubbleTea("딸기요거트", 3500), BubbleTea("타로밀크티", 3500)]

    def __init__(self):
        self.order_menu = []
        self.order = None

    def show_menu(self):
        print("<Menu>\n0: 아메리카노 1800원, 1: 딸기요거트 3500원, 2: 타로밀크티 3500원")

    def sum_price(self):
        sum = 0
        for drink in self.order_menu:
            sum += drink.price

        return sum

    def order_drink(self):
        # 반복
        # 메뉴 보여주기
        # 주문 받기 -> 음료 선택 -> 음료 객체 생성
        # 옵션 선택 -> 컵 사이즈 얼음량 당도 펄
        # 주문한 음료 리스트에 추가
        # 주문한 음료 출력
        # 금액 합계 출력
        while True:
            self.show_menu()
            self.order = input("음료를 선택하세요 : ")
            if self.order == "":
                break
            drink = Order._menus[int(self.order)]
            drink.order()
            self.order_menu.append(drink)
            print("주문 음료 - ", drink, "\n")

        print("\n<Order List>")
        for drink in self.order_menu:
            print("주문 음료 - ", drink)
        print("\n총 금액 : ", self.sum_price(), "원")


o = Order()
o.order_drink()

# <테스트코드>
# 아메리카노 = Coffee("아메리카노", 1800)
# # 아메리카노.set_cup()
# # 아메리카노.set_ice()
# # 아메리카노.set_sugar()
# 아메리카노.order()
# print("\n", 아메리카노, "\n\n\n")           #이름 : 아메리카노      가격 : 1800원

# 타로밀크티 = BubbleTea("타로밀크티", 3500)
# #타로밀크티.set_cup()
# #타로밀크티.set_ice()
# #타로밀크티.set_sugar()
# #타로밀크티.set_Pearl()
# 타로밀크티.order()
# print("\n", 타로밀크티)