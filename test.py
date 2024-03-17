import requests

url = 'http://127.0.0.1:8000/answer/'
data = {
    'question': 'Hi, I have a slight body pain after gym',
    'keywords': 'gym, pain, body',
    'num_results': 30
}

response = requests.post(url, data=data)
print(response.json())
