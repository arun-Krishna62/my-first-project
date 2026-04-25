print("Temperature Converter!")
choice = input("\n1.Celsius to Farenheit\n2. Farenheit to Celsius\nEnter choice:")
if choice == "1":
    celsius = float(input("Enter Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}C = {fahrenheit:.2f}F")

elif choice == "2":
    fahrenheit = float(input("Enter Fahremheit:  "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit} F = {celsius:.2f} C")

else:
    print("Invalid choice!")