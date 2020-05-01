import requests

IP_ADDR = '192.168.1.90'
PORT = 5000

image_data = open("couple.jpg","rb").read()

response = requests.post(f"http://{IP_ADDR}:{PORT}/v1/vision/detection", files={"image":image_data})

print(response.json())