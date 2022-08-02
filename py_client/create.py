import requests

headers={'Authorization': 'token 401623800faa0cb6da91b759eaaf010bf37465b3'}
endpoint  = "http://localhost:8000/api/products/" 
data={
    "title":"This is a field title",
    "price":32.99
}
get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())