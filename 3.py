def inches_to_centimeters(height_in_inches):
    return height_in_inches * 2.54

# Using Nested Interactive Loop
def convert_heights_nested_loop():
    num_customers = int(input("Enter the number of customers: "))
    heights_inches = []

    # Input heights in inches
    for i in range(num_customers):
        height = float(input(f"Enter height (in inches) for customer {i + 1}: "))
        heights_inches.append(height)

    # Convert heights to centimeters using nested loop
    heights_centimeters = []
    for height_in_inches in heights_inches:
        height_in_cm = inches_to_centimeters(height_in_inches)
        heights_centimeters.append(height_in_cm)

    return heights_centimeters

# Using List Comprehensions
def convert_heights_list_comprehension():
    num_customers = int(input("Enter the number of customers: "))
    
    # Input heights in inches using list comprehension
    heights_inches = [float(input(f"Enter height (in inches) for customer {i + 1}: ")) for i in range(num_customers)]

    # Convert heights to centimeters using list comprehension
    heights_centimeters = [inches_to_centimeters(height_in_inches) for height_in_inches in heights_inches]

    return heights_centimeters

# Example using Nested Interactive Loop
print("Using Nested Interactive Loop:")
heights_nested_loop = convert_heights_nested_loop()
print("Heights in Centimeters:", heights_nested_loop)

# Example using List Comprehensions
print("\nUsing List Comprehensions:")
heights_list_comprehension = convert_heights_list_comprehension()
print("Heights in Centimeters:", heights_list_comprehension)

