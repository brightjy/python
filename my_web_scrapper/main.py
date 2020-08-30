import requests


thebell_result = requests.get("https://www.thebell.co.kr/free/index.asp")

print(thebell_result.text)