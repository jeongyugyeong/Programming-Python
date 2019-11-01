from order import Order
from file_manager import FileManager

# 주문 내역 불러 오고, 보여 주기
file_manager = FileManager("history.bin")
# answer = input("주문내역을 볼 건가요? (y or n) ")
# if answer == "y":
history = []

try:
    history = file_manager.load()
    # 여기에서 history를 가져오지 못 하더라도, 위에서 history을 선언해 주었기 때문에 정상적으로 됨.
    sum = 0
    for h in history:
        print(h)
        sum += h.price
    print()
    print("지금까지 아마스빈에서 사용한 금액은 " + str(sum) + " 원입니다.")
    print()
except FileNotFoundError:
    print("주문내역이 없습니다.")
    print()

o = Order()
o.order_drink()

# 주문 내역 저장하기
file_manager.save(history + o.order_menu)