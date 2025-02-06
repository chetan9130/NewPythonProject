n = int(input("Enter a number: "))
upto = int(input("Enter table limit: "))

for i in range(1, upto + 1):
    print(f"{n} x {i} = {n * i}")
