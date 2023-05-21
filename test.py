import requests
url="http://localhost:5000/add"
payload={'name':'Wilson',
         'number':'163363',
         'email':'bjbz@ssdgy',
         'social_media':'dhvs',
         'reason':'shbvas'}
response=requests.post(url,data=payload,verify=False,cert=None)
print(response.status_code)