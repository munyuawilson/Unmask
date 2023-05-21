import requests
url = 'http://localhost:5000/search'
data = {
    'number':163363
}


response = requests.get(url, data=data)
print(response.status_code)
print(response.json)
