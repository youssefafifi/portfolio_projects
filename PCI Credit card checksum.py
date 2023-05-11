def luhn_checksum(card_number):
    digits = [int(d) for d in str(card_number)]
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    total = sum(odd_digits)
    for d in even_digits:
        d *= 2
        if d > 9:
            d -= 9
        total += d
    return total % 10

def is_valid_card(card_number):
    return luhn_checksum(card_number) == 0

def main():
    card_number = input("Enter your credit card number: ")
    if is_valid_card(card_number):
        print("The credit card number is valid.")
    else:
        print("The credit card number is invalid.")

if __name__ == "__main__":
    main()
