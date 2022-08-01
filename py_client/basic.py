import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint  = "http://localhost:8000/api/" 
get_response = requests.get(endpoint,json={"product_id":123}) #HTTP REQUEST
print(get_response.headers)
print(get_response.status_code) #HTTP STATUS CODE 
print(get_response.text) #RAW DATA
# print(get_response.json()['message']) #JSON 
# print(get_response.json()) #JSON 

# HTTP REQUEST -> HTML
# API HTTP REQUEST -> JSON

# {
#   "args": {},
# *  "data": "{\"query\": \"Hello world\"}", //  'data': '' json = 
# *  "files": {}, // 'form': {'query': 'Hello world'} * data=
#   "form": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Content-Length": "24",
#     "Content-Type": "application/json",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.28.1",
#     "X-Amzn-Trace-Id": "Root=1-62e814ef-0ca8fb7420fb152c2863c7f2"
#   },
#   "json": {
#     "query": "Hello world"
#   },
#   "method": "GET",
#   "origin": "41.230.76.21",
#   "url": "https://httpbin.org/anything"
# }
#print(get_response.json()) #JSON 

# {'args': {}, 'data': '{"query": "Hello world"}', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '24', 'Content-Type': 'application/json', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.28.1', 'X-Amzn-Trace-Id': 'Root=1-62e814ef-0ca8fb7420fb152c2863c7f2'}, 'json': {'query': 'Hello world'}, 'method': 'GET', 'origin': '41.230.76.21', 'url': 'https://httpbin.org/anything'}