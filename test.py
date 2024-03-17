import requests

url = 'https://8000-hackoversho-doctorcopil-bl0n7lgytuh.ws-us110.gitpod.io/answer/'
data = {
    'question': 'Hi, I have a slight body pain after gym',
    'keywords': 'gym, pain, body',
    'num_results': 30
}

response = requests.post(url, data=data)
print(response.json())
