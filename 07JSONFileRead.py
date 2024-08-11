import json

file = open('myphone.json','r')
data = json.load(file)

print(data)
file.close()

print('MODEL : ',data['model'])     
print('PRICE : ',data['price'])