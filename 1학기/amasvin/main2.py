from order import Order
from file_manager2 import FileManager

sum = 0

# 주문 내역 불러 오고, 보여 주기
file_manager = FileManager("history.bin")
history = file_manager.load()
if len(history) == 0:
    print("주문 내역이 없습니다.")
    print()
else:
    for h in history:
        print(h)
        sum += h.price
print()
print("지금까지 아마스빈에서 사용한 금액은 " + str(sum) + " 원입니다.")
print()

# 주문하기
o = Order()
o.order_drink()

# 주문 내역
file_manager.save(history + o.order_menu)