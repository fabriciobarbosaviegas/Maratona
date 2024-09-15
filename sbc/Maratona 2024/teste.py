import requests
import json

url = "https://solida-app-lb1t.onrender.com/report"

payload = {}
headers = {
  'Authorization': 'Bearer oat_MjM.bFJJUmdTd0JBMlY2X1oyNkVqSVZ1ZXdyendGS0Q2bmhaODZIOUh0bTEyNzUzNjc5MTk'
}

response = requests.request("GET", url, headers=headers, data=payload)

response = response.json()

for i in response:
    res = requests.request("DELETE", url+'/'+str(i['id']), headers=headers, data=payload)

    print(res.text)