import requests
import re

url = 'https://jsonplaceholder.typicode.com/users'
request = requests.get(url)
response = request.json()

phone_numbers = []
for i in response:
  phone_numbers.append(i['phone'])
  #print(i['phone'])

result = []
for number in phone_numbers:
  has_x = re.search(r'x\d+', number)
  has_dot = re.search(r'\d\.\d', number)
  
  if not has_x and not has_dot:
    result.append(number)

print('Correct numbers: ')
for i in result:
  print(i)


