import requests

endpoint  = "http://localhost:8000/api/products/1546146/" 
get_response = requests.get(endpoint,json={"title":"Abc123","content":"This is a title","price":"abc134"}) #HTTP REQUEST
print(get_response.json()) #JSON 