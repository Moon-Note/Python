import requests 

url = "http://www.google.co.kr" 
response = requests.get(url) 
print('정상적으로 url로부터 Response를 받으면 "200" 출력, 결과 : ', response.status_code) 
print('출력 응답 :')
print(response.text)