# Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

# Display message explaining code action
print ('Printing sum of previous and current number in a range (10)...')

# Set 0 as the previous number to start the loop
previous_number = 0 

# Run through the numbers in the range (10)
for current_number in range (0,10):

    # Calculate sum of current number and previous number 
    sum = current_number + previous_number

    # Display current number, previous number, and their sum.
    print ('Current Number:', current_number, 'Previous Number:', previous_number, "Sum:", sum)

    previous_number = current_number
