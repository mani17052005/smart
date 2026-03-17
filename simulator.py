import requests
import random
import time

url = "http://127.0.0.1:5000/api/sensordata"

while True:

    data = {
        "temperature": random.randint(30,36),
        "pressure": random.randint(40,70),
        "steps": random.randint(0,200),
        "glucose": random.randint(90,140)
    }

    requests.post(url,json=data)

    print("Data Sent:",data)

    time.sleep(3)