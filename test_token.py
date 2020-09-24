import requests

TOKEN = 'b3553e77d0353f0d86b95f163e96b6363c9f9a4e'

headers = {
    'Authorization': f'Token {TOKEN}',
}

res = requests.get("http://localhost:8000/post/1/", headers=headers)

print(res.json())