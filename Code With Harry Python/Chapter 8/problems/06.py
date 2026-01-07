def print_star_pattern():
    # Top half
    for i in range(1, 20):
        print("*" * i)
    
    # Bottom half
    for i in range(18, 0, -1):
        print("*" * i)

# Call the function
print_star_pattern()
