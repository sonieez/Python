#at least one letter [a-z]
#at least one number [0-9]
#[A-Z] [$@#] minimum 6, maximum 12

import re

password = input('Enter your password: ')

patterns = [r'.{6,12}', r'[a-z]', r'[A-Z]', r'[0-9]', r'[$@#]']

conditions = True

for pattern in patterns:
  if re.search(pattern, password):
    print('Condition satisfied')
  else:
    conditions = False
    print('Condition not satisfied')

print('Password is acceptable' if conditions else 'Password is not accepted')
