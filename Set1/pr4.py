numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))

if numbers:
    avg = sum(numbers) / len(numbers)
    print(f"Average: {avg}")
else:
    print("No numbers entered.")
