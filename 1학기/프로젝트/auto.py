#PyAutoGUI 설치하자
#pip install pyautogui

import pyautogui as pag
if __name__ == '__main__':
#     while True: #좌표 구하기
#         x, y = pag.position()
#         print("x: {}\ty: {}".format(x, y), end="\r")
pag.moveTo(484, 44, duration=2)
pag.doubleClick(484,44,duration=2)
time.sleep(1) #크롬이 열리기를 기다려야함
page.typewrite("http://interpark.com/")
pag.press("enter")
