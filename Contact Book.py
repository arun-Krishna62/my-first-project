contacts = []

print("Welcome to Contact Book!")
choice = input("\n1. Add Contact \n2. Show All\n3. Search\nEnter choice: ")
if choice == "1":
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    contacts.append({"name" : name, "phone": phone})
    print(f"{name} added successfully!")

elif choice == "2":
    if len(contacts) == 0:
        print("No contacts found!")
    else:
        for contact in contacts:
            print(f"Name: {contact['name']} | Phone: {contact['phone']}")

elif choice == "3":
    search = input("Enter name to search: ")
    for contact in contacts:
        if contact['name'].lower() == search.lower():
            print(f"Found! Phone: {contact['phone']}")
            break
    else:
        print("Contact not found!")

else:
    print("Invalid choice!")