import re

def validate_credit_card(card_number):
    # Remove non-numeric characters from the card number
    card_number = re.sub(r'\D', '', card_number)
    
    # Implement the Luhn algorithm to validate the card number
    digits = list(map(int, card_number))
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    
    total = sum(odd_digits)
    
    for digit in even_digits:
        total += sum(divmod(digit * 2, 10))
    
    return total % 10 == 0

# Accept a credit card number as input
card_number = input("Enter a credit card number: ")

# Validate the credit card number
if validate_credit_card(card_number):
    print("Valid credit card!")
else:
    print("Invalid credit card!")