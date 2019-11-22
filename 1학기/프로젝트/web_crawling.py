from bs4 import BeautifulSoup #html 구조적으로 변환하자
from urllib.request import urlopen #url에 해당하는 html 가져오자

if __name__ == '__main__':
    data = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=651673")
    soup = BeautifulSoup(data, "lxml")
    print(soup)
    cartoon_titles = soup.find_all("td", attrs={'class':'title'})   #<td class="title>
    html = "<html><head><meta charset='utf-8'></head></body>"
    for title in cartoon_titles:
        t = title.find('a').text   #제목 가져오자
        link = title.find('a').get("href")
        link = "http://comic.naver.com/"+link
        # print(t)
        # print(link)
        html+="<a href='"+link+"'>"+t+"</a><br><br>"
    html+="</body></html>"
    outputSoup = BeautifulSoup(html, "lxml")  #htmlstring -> Beautiful Soup 객체
    prettyHtml = str(outputSoup.prettify())   #html 줄 예쁘게
    with open("유미의세포들.html", "w", encoding="utf-8")as f:
        f.write(prettyHtml)

# data = urlopen("http://webtoon.daum.net/webtoon/view/findjuly")
# soup = BeautifulSoup(data, "lxml")
# print(soup)
# cartoon_titles = soup.find_all("strong", attrs={"class":"tit_wt"})
# for title in cartoon_titles:
#     print(title)
