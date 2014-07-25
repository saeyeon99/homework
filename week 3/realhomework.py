import urllib
from bs4 import BeautifulSoup

htmltext = urllib.urlopen("http://api.sbs.co.kr/xml/news/rss.jsp?pmDiv=external").read()

soup = BeautifulSoup(htmltext, from_encoding="utf-8")

authors = []

for item in soup.select("item"):
	authors.append(item.get_text())			# (원래 예제) 작성자 이름만 가져오기
#	authors.append(item.parent.get_text())	# 작성자 태그의 부모요소의 text만 가져오기
#	authors.append(item.findChildren())		# 작성자 태그의 자식요소만 가져오기

for author in authors:
	print author