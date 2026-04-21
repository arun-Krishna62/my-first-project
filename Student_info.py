def student_info():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    city = input("Enter city: ")
    movie = input("Favourite movie: ")
    student = {"name": name, "age": age, "city": city, "movie": movie}
    print(student["name"])
    print(student["age"])
    print(student["city"])
    print(student["movie"])

student_info()