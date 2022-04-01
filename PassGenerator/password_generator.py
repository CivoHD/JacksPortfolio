import random
import string

length = int(input("Enter the length you want your password: "))
amount = int(input("Enter the amount of passwords you want: "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

all = lower + upper + digits + symbols


for i in range(amount):
    password_generate = random.sample(all, length)
    password = ''.join(password_generate)
    print(password)