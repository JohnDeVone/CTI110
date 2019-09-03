# This is an assignment calculating the tip of a meal including tax as well
# Sept 3, 2019
# CTI-110 P2HW1 - Meal Tip Tax Calculator
# John DeVone
#

# Ask for the charge of food
subtotal = float(input('Enter the total cost of the food: '))

# Ask for the percentage the customer would like to tip
tip_percent = float(input('What is the percentage you want to tip? (Enter it as a decimal. Example: 23% = .23):'))

# Ask for the tax amount of the transaction
tax_percent = float(input('What is the tax percentage of the transaction? (Use the same decimal format as the last question.):'))

# Calculate the tip and tax
calc_tip = tip_percent * subtotal
calc_tax = tax_percent * subtotal
total = subtotal + calc_tip + calc_tax

# Display the calculations
print('The total tip amount will is $ ', format(calc_tip, ',.2f'))
print('The total tax amount will is $ ', format(calc_tax, ',.2f'))
print('The total of your meal including tax and tip will is $ ', format(total, ',.2f'))
