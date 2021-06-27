import pandas as pd
from bs4 import BeautifulSoup
import json
import requests
from urllib.parse import urlencode, unquote, quote_plus

# 시크릿 키 가져오기 
with open("key.json","r") as file: 
    key = json.load(file)

# 검색할 단어 입력 받기 
search = str(input("검색어를 입력하세요."))

# print(search)
url = 'https://stdict.korean.go.kr/api/search.do'

# 파라미터 설정
params = '?' + urlencode({
    'certkey_no' : '2802',
    'key' : key['SECRET_KEY'],
    'type_search':'search',
    quote_plus('q') : search
})

response = requests.get(url + unquote(params))
# 결과 값을 string 으로 저장 
textres = response.text

# xml 형식 인식을 위해 Beautifulsoup 사용 
soup = BeautifulSoup(textres, 'html.parser')

# definition 태그 값을 찾아 모두 value 에 저장 
value = soup.find_all('definition')
# print(response.url)

# for 문을 돌면서 슬라이싱 하여 입력한 단어의 뜻(여러 개가 나올 때)만을 출력
for i in value : 
    # 뜻을 worddef 안에 문자열로 저장
    worddef = str(i)
    # index = worddef.find("CDATA")
    # 뜻 맨 끝에는 항상 닫는 ]] 가 있어 이 문자를 기준으로 슬라이싱 진행. 
    index2 = worddef.find("]]")
    # 슬라이싱을 한 후 단어의 뜻만을 final 변수에 저장 
    final = worddef[21:index2]
    # print(index)
    # print(index2)
    print(final)

# def api (dic) : 
#     return dic 