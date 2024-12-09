# Function to convert Roman numeral to decimal
def roman_to_decimal(roman):
    # Dictionary for Roman numeral values
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0  # Track the previous Roman numeral value to handle subtractive notation

    # Loop through the Roman numeral in reverse order
    for char in reversed(roman):
        current_value = roman_values[char]  # Get the current Roman numeral value
        if current_value < prev_value:  # If the current value is less than the previous, subtract it
            total -= current_value
        else:
            total += current_value  # Otherwise, add it to the total
        prev_value = current_value  # Update previous value for next iteration

    return total  # Return the decimal value of the Roman numeral

# Function to convert decimal number to words
def decimal_to_words(number):
    # Check if number is zero, return "Zero" as the word
    if number == 0:
        return "Zero"

    # Lists to store words for different number ranges
    units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "One Thousand", "Two Thousand", "Three Thousand", "Four Thousand", "Five Thousand", "Six Thousand", "Seven Thousand", "Eight Thousand", "Nine Thousand"]
    ten_thousands = ["", "Ten Thousand", "Twenty Thousand", "Thirty Thousand", "Forty Thousand", "Fifty Thousand", "Sixty Thousand", "Seventy Thousand", "Eighty Thousand", "Ninety Thousand"]
    
    # Handle hundreds of thousands and larger numbers
    hundred_thousands = ["", "One Hundred Thousand", "Two Hundred Thousand", "Three Hundred Thousand", "Four Hundred Thousand", "Five Hundred Thousand", "Six Hundred Thousand", "Seven Hundred Thousand", "Eight Hundred Thousand", "Nine Hundred Thousand"]
    millions = ["", "One Million", "Two Million", "Three Million", "Four Million", "Five Million", "Six Million", "Seven Million", "Eight Million", "Nine Million"]

    result = []  # List to hold the words for each part of the number

    # Check if the number is negative
    if number < 0:
        result.append("Negative")  # Add "Negative" if the number is negative
        number = abs(number)  # Make the number positive for easier processing

    # Process each place value from millions down to units
    if number >= 1000000:
        result.append(millions[number // 1000000])  # Add millions part
        number %= 1000000  # Update number to process the remaining part

    if number >= 100000:
        result.append(hundred_thousands[number // 100000])  # Add hundred-thousands part
        number %= 100000

    if number >= 10000:
        result.append(ten_thousands[number // 10000])  # Add ten-thousands part
        number %= 10000

    if number >= 1000:
        result.append(thousands[number // 1000])  # Add thousands part
        number %= 1000

    if number >= 100:
        result.append(units[number // 100] + " Hundred")  # Add hundreds part
        number %= 100

    # Process tens and ones parts
    if number // 10 == 1:  # Check if the tens digit is 1 (for "teens")
        result.append(teens[number % 10])  # Add the corresponding teen word
    else:
        if number // 10 > 0:
            result.append(tens[number // 10])  # Add tens part if greater than zero
        if number % 10 > 0:
            result.append(units[number % 10])  # Add ones part if greater than zero

    # Join the list into a single string and return
    return ' '.join(result)

# Function to perform arithmetic operations
def perform_operation(num1, num2, oper):
    # Check for each operation and return the result
    if oper == '+':
        return num1 + num2  # Addition
    elif oper == '-':
        return num1 - num2  # Subtraction
    elif oper == '*':
        return num1 * num2  # Multiplication
    elif oper == '/':
        return num1 // num2 if num2 != 0 else 0  # Division (return 0 if dividing by zero)
    return 0  # Return 0 for unsupported operations

# Function to process each line in the input file
def process_line(line):
    # Split the line into parts (numbers and operators)
    parts = line.split()
    total_result = 0  # Initialize total result for the line
    first_operation = True  # Flag to check if it's the first operation in the line

    # Process each part (operand and operator)
    for i in range(0, len(parts), 3):
        roman1 = parts[i]  # First Roman numeral
        oper = parts[i + 1]  # Operator
        roman2 = parts[i + 2]  # Second Roman numeral

        # Convert Roman numerals to decimals
        num1 = roman_to_decimal(roman1)
        num2 = roman_to_decimal(roman2)

        # Perform the operation between the two numbers
        result = perform_operation(num1, num2, oper)

        # If it's the first operation, initialize the total result
        if first_operation:
            total_result = result
            first_operation = False
        else:
            # Perform subsequent operations using the total result so far
            total_result = perform_operation(total_result, result, oper)

    # Convert the final result to words and return it
    return decimal_to_words(total_result)

# Read the input file, process the lines, and write to the output file
def main():
    # Open the input and output files
    with open("Input.txt", "r") as input_file, open("Output.txt", "w") as output_file:
        # Process each line in the input file
        for line in input_file:
            line = line.strip()  # Remove leading/trailing whitespaces
            if line:  # Only process non-empty lines
                result_in_words = process_line(line)  # Process the line and convert result to words
                output_file.write(result_in_words + "\n")  # Write result to output file

    print("Processing complete. Check Output.txt for results.")  # Print completion message

# Call the main function when the script is executed
if __name__ == "__main__":
    main()
