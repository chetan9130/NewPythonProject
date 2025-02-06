import random

length = int(input("Enter password length: "))
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"

password = "".join(random.choice(chars) for _ in range(length))

print(f"Generated Password: {password}")
