# 2418 정유경
# 운명을 믿으시나요(8문 8답)
# 질문을 통해서 가장 잘 맞는 사람을 순위로 내주는 프로그램입니다.

tempts = ["지금의 연인", "이상형"]

#for 문을 이용하여 tempts 안의 선택 사항을 모두 출력합니다.
print "연애하고 있지만 당신의 이상형이 나타나서 고백을 했을 때, 당신의 선택은 ?"
for tempt in tempts:
	print tempt

# 사용자에게 어떤 선택을 할지 질문을 출력합니다.
print "연애하고 있지만 당신의 이상형이 나타나서 고백을 했을 때, 당신의 선택은 ?"
choice = raw_input()

#while 문을 이용하여 선택 목록에 없을 시에는 다시 입력받습니다.
while choice not in tempts:
	print "다시 선택해 주세요."
	choice = raw_input()



ages = ["연상", "동갑", "연하"]

print "당신의 취향은 ?"
for age in ages:
	print age

print "당신의 취향은 ?"
choice = raw_input()

while choice not in ages:
	print "다시 선택해 주세요."
	choice = raw_input()



perfects = ["믿는다", "믿지 않는다", "믿진 않지만 신경은 쓰인다"]

print "당신은 궁합을 믿는 편인가 ?"
for perfect in perfects:
	print perfect

print "당신은 궁합을 믿는 편인가 ?"
choice = raw_input()

while choice not in perfects:
	print "다시 선택해 주세요."
	choice = raw_input()



breakups = ["카톡이나 전화로 이별통보", "희망고문을 주는 애매한 말로 헤어짐", "잠수", "바람피고 이별통보"]

print "다음 중 당신이 최악이라 생각하는 이별 방법은 ?"
for breakup in breakups:
	print breakup

print "다음 중 당신이 최악이라 생각하는 이별 방법은 ?"
choice = raw_input()

while choice not in breakups:
	print "다시 선택해 주세요."
	choice = raw_input()



kicks = ["차는 편", "차이는 편"]

print "당신은 차는 편 ? 차이는 편 ?"
for kick in kicks:
	print kick

print "당신은 차는 편 ? 차이는 편 ?"
choice = raw_input()

while choice not in kicks:
	print "다시 선택해 주세요."
	choice = raw_input()



friends = ["우정", "사랑"]

print "알고보니 절친과 같은 사람을 좋아하고 있었다. 당신의 선택은 ?"
for friend in friends:
	print friend

print "알고보니 절친과 같은 사람을 좋아하고 있었다. 당신의 선택은 ?"
choice = raw_input()

while choice not in friends:
	print "다시 선택해 주세요."
	choice = raw_input()



winters = ["겨울 분위기의 쇼핑몰", "분위기 좋은 카페", "스키장", "크리스마스 분위기가 나는 놀이공원"]

print "당신이 겨울에 데이트를 한다면 어디로 갈 것 인가 ?"
for winter in winters:
	print winter

print "당신이 겨울에 데이트를 한다면 어디로 갈 것 인가 ?"
choice = raw_input()

while choice not in winters:
	print "다시 선택해 주세요."
	choice = raw_input()



dates = ["카페", "영화관", "분위기 좋은 바", "공원"]

print "당신이 첫 데이트를 하고 싶은 장소는 ?"
for date in dates:
	print date

print "당신이 첫 데이트를 하고 싶은 장소는 ?"
choice = raw_input()

while choice not in dates:
	print "다시 선택해 주세요."
	choice = raw_input()