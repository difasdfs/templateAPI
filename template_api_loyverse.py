import requests
import json

no_struk = "44-8294"
baseUrl = 'https://api.loyverse.com/v1.0/receipts/'
access_token = '4a3e5665ac324711b13d677c8c05cac8'
header = {'Authorization' : 'Bearer ' + access_token}

payload = {
    "since_receipt_number" : no_struk,
    'limit' : 250
    }

respon = requests.get(baseUrl, headers=header, params=payload)
hasil = json.loads(respon.text)
    
while True:
    if "cursor" in hasil.keys():
        respon = requests.get(baseUrl, headers=header, params={"cursor" : hasil['cursor']})
        hasil = json.loads(respon.text)
    else:
        break