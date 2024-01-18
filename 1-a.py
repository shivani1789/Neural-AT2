def fullname(first_name, last_name):
    return f"{first_name} {last_name}"

                 # Taking user input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

             # Calling the fullname function
full_name = fullname(first_name, last_name)

               # Displaying the result
print("Full Name:", full_name)
