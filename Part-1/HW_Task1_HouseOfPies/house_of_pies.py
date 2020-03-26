print("\nWelcome to the House of Pies! Here are our pies: ")

# Create list of pies
pie_types = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun", "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

# Print pie options available for user selection
for pie in pie_types:
    pie_location = pie_types.index(pie) + 1 
    print("(" + str(pie_location) + ")" + " " + pie)

# Create a list to track pies selected and set initial values to 0; index of list to correspond with index of pie_types list
pie_counter = [0 for pie in pie_types]

# Initialize variable for use in determining when to terminate while loop
more = 'y'

# Perform operations for as long as the user answers (y)es
while more == 'y':
    
    # Request user to select a pie
    pie_choice = int(input("Which pie would you like to order? "))
    
    # Determine corresponding index in pie_types and pie_counter of selected pie
    pie_choice = pie_choice - 1
    
    # Count each time a specific type of pie is selected
    pie_counter[pie_choice] = pie_counter[pie_choice] + 1
    
    print(f"Great! We'll have that {pie_types[pie_choice]} pie right out for you.")
    
    # Prompt whether user would like to order another pie
    more = input("Would you like to make another order? (y)es or (n)o? ")

# Zip lists
pie_order = zip(pie_counter, pie_types)

# Set initial value of total pie counter variable to 0
pie_total = 0

# Calculate total number of pies based on user input
for pie in pie_counter:
    pie_total = pie_total + pie

# Determine message to show user based on total number of pies chosen
if pie_total == 1:
    print(f"\nYou purchased {pie_total} pie.")
else:
    print(f"\nYou purchased {pie_total} pies total.")

# Print summary of user selection
print("You purchased: ")
for pie in pie_order:
    print(f"{pie[0]} {pie[1]}")
