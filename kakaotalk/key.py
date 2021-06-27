import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = 'dfbe80d49cb551a672ddb6c3c20d30c6'
redirect_uri = 'https://example.com/oauth'
authorize_code = '27JYbzsdu3xvYXk8iZq0F5Ik8-_rM3nOmHjggmkQU458HfyJbNaVlYrpfXei3RNmdaLdXgo9dRoAAAF6OQdK8A'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json
#1.
# with open(r"C:\Users\user\Desktop\PythonWorkspace\kakao_test\kakao_code.json","w") as fp:
#     json.dump(tokens, fp)

#2.
with open("kakao_code.json","w") as fp:
    json.dump(tokens, fp)