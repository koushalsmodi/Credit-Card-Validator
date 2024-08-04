from cs50 import get_int


def main():
    while True:
        # Get input for credit card number
        credit_card = get_int('Number: ')
        if credit_card >= 0:
            break  # Continue asking for valid input until a non-negative number is entered

    # Check the validity of the credit card number using Luhn's algorithm
    if check_validity(credit_card):
        # If valid, print the card brand
        print_card_brand(credit_card)
    else:
        # If invalid, print "INVALID"
        print('INVALID')

def main():
    while True:
        credit_card = get_int("Number: ")
        if credit_card >= 0:
            break

    if check_validity(credit_card):
        print_card_brand(credit_card)

    else:
        print('Invalid')

    
def check_validity(credit_card_number):
    # Convert the credit card number to a list of digits in reverse order
    reversed_digits = [int(digit) for digit in str(credit_card_number)][::-1]

    # Calculate the checksum using Luhn's algorithm
    total = sum(get_luhn_digit(digit, index) for index, digit in enumerate(reversed_digits))

    # Check if the total checksum is divisible by 10
    return total % 10 == 0

def get_luhn_digit(digit, index):
    # Apply Luhn's algorithm to each digit based on its position in the credit card number
    if index % 2 != 0:
        doubled_digit = 2 * digit
        return doubled_digit if doubled_digit < 10 else doubled_digit - 9
    return digit

def print_card_brand(credit_card_number):
    # Convert the credit card number to a string to check its length and starting digits
    card_number_str = str(credit_card_number)
    length = len(card_number_str)

    # Identify the credit card brand based on the length and starting digits
    if length == 15 and (card_number_str.startswith('34') or card_number_str.startswith('37')):
        print('AMEX') # American Express
    elif length == 16 and 51 <= int(card_number_str[:2]) <= 55:
        print('MASTERCARD') # Mastercard
    elif (length == 13 or length == 16) and card_number_str.startswith('4'):
        print('VISA') # Visa
    else:
        print('INVALID') # Invalid card brand

if __name__ == '__main__':
    main()
