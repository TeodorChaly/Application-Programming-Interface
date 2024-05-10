import requests

# Connecting to the API_Learn

r = requests.get("http://127.0.0.1:8000/hotels/12")
print(r.json())
