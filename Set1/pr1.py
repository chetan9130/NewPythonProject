while True:
    choice = input("Convert (C to F) or (F to C)? Enter 'C' or 'F': ").strip().upper()

    if choice == "C":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")
    elif choice == "F":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"Temperature in Celsius: {celsius:.2f}")
    else:
        print("Invalid choice. Please enter 'C' or 'F'.")

    if input("Convert another? (yes/no): ").strip().lower() != "yes":
        print("Goodbye!")
        break
