import argparse
import string
import random

def generate_password(username, platform, pin):
    # Set random seed based on input values
    seed_str = username + platform + pin
    seed = int.from_bytes(seed_str.encode(), 'little')
    random.seed(seed)

    # Define character sets for password
    upper_chars = string.ascii_uppercase
    lower_chars = string.ascii_lowercase
    digit_chars = string.digits
    symbol_chars = "!#$%&()*+,-./:;<=>?@[]^_`{|}~"

    # Combine character sets to form pool of characters to choose from
    char_pool = upper_chars + lower_chars + digit_chars + symbol_chars

    # Create password
    password = ''.join(random.choice(char_pool) for _ in range(24))

    return password

def main():
    parser = argparse.ArgumentParser(description='Generate a secure password.')
    parser.add_argument('-u', '--username', type=str, help='Username', required=True)
    parser.add_argument('-s', '--service', type=str, help='Service', required=True)
    parser.add_argument('-p', '--pin', type=str, help='PIN', required=True)
    args = parser.parse_args()

    password = generate_password(args.username, args.service, args.pin)

    print(f'Generated Password: {password}')

if __name__ == '__main__':
    main()
