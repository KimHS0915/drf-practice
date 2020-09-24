import requests

# TOKEN = 'b3553e77d0353f0d86b95f163e96b6363c9f9a4e'
JWT_TOKEN = (
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9."
    "eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6InRlc3R1c2VyMyIsImV4cCI6M"
    "TYwMDk4MjI2MiwiZW1haWwiOiIiLCJvcmlnX2lhdCI6MTYwMDk4MTk2Mn0."
    "QnG3D3VcYJ2WuLafydPfzVvCahMqqRFhstnf1KIXBj0"
)

headers = {
    # 'Authorization': f'Token {TOKEN}',
    'Authorization': f'JWT {JWT_TOKEN}',
}

res = requests.get("http://localhost:8000/post/1/", headers=headers)

print(res.json())