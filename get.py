import requests

url = 'http://localhost:5000/predict'
data = {'text': 'Sir, jyada sentimental mat ho jao peene ke baad.Jiss desh ki buniyad sirf Hindu hatred pe hui ho woh kabhi nahi sudrega. Aap POK de do yaa phir Kabootar udao, jawab sirf goliyon se milega....'}

response = requests.post(url, json=data)

print(response.json())

