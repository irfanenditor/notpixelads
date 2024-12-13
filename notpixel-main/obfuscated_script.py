import os
import json
import re
from datetime import datetime

# Clear screen function
def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux/Unix/Mac
        os.system('clear')

# Print colored message
def print_green(message):
    print(f"\033[1;32m{message}\033[0m")

# Extract ID from referral link
def extract_referral_id(link):
    match = re.search(r'startapp=f(\d+)', link)
    if match:
        return match.group(1)
    return None

# Clear screen initially
clear_screen()

# Print welcome messages
print_green(". Open Not Pixel")
print_green(". Copy your Not Pixel referral links (one per line)")
print_green(". Type 'done' when you have pasted all links")

# File to store user data
users_file = 'users.json'

# Load users from the file if it exists
if os.path.exists(users_file):
    with open(users_file, 'r') as f:
        users = json.load(f)
else:
    users = {}

while True:
    print_green("Paste your Not Pixel referral links one by one (type 'done' to finish):")
    links = []
    while True:
        referral_link = input().strip()
        if referral_link.lower() == 'done':  # Stop input on "done"
            break
        if referral_link:
            links.append(referral_link)

    for referral_link in links:
        user_id = extract_referral_id(referral_link)

        if not user_id:
            print_green(f"Error: Invalid Not Pixel referral link: {referral_link}")
            continue

        if user_id in users:
            print_green(f"Error: ID already saved! User ID: {user_id}")
            continue

        users[user_id] = {
            'tg_id': user_id,
            'saved_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        print_green(f"Success: ID saved! User ID: {user_id}")

    # Save updated users to file
    with open(users_file, 'w') as f:
        json.dump(users, f, indent=4)

    print_green("\nDo you want to save more referral links? (y/n):")
    continue_input = input().strip().lower()

    if continue_input != 'y':
        break

print_green("\nSaved IDs:")
print(json.dumps(users, indent=4))
