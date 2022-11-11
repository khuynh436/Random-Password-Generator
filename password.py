### Generate randomize password
### Import necessary packages

import random
import string

# Strings
lower_case = 'abcdefghijklmnoqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '~!@#$%^&*()<>?/.,'

# Combine
use_for = lower_case + upper_case + numbers + symbols

# Length of string
length_password = 15

# Random generated string
password = "".join(random.sample(use_for, length_password))

# Results
print("Your Password Is:", password)






