p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))
si = (p*r*t) / 100

print(f"Simple Interest: {si:.2f}")
print(f"Total Amount: {p + si:.2f}")