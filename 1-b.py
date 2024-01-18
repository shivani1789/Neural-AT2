def string_alternative(full_name):
    return full_name[::2]

# Example usage with the provided string "Good evening"
example_str = "Good Morning"
result = string_alternative(example_str)

# Displaying the result
print("Original String:", example_str)
print("Every Other Character:", result)
