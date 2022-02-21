import random

length=int(input("Enter the length of the password required: "))

password=''

for n in range(length):
    n = chr(random.randint(33,126))
    password=str(password) + n
    
print(password)