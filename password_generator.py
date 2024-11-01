import random
import string

password_gen_text = """
  ______    ______    _______  _______  __   __   __   ______    ______    ____$$ |        ______    ______   _______    ______    ______   ______   _$$ |_     ______    ______  
 /      \  /      \  /       |/       |/  | /  | /  | /      \  /      \  /    $$ |       /      \  /      \ /       \  /      \  /      \ /      \ / $$   |   /      \  /      \ 
/$$$$$$  | $$$$$$  |/$$$$$$$//$$$$$$$/ $$ | $$ | $$ |/$$$$$$  |/$$$$$$  |/$$$$$$$ |      /$$$$$$  |/$$$$$$  |$$$$$$$  |/$$$$$$  |/$$$$$$  |$$$$$$  |$$$$$$/   /$$$$$$  |/$$$$$$  |
$$ |  $$ | /    $$ |$$      \$$      \ $$ | $$ | $$ |$$ |  $$ |$$ |  $$/ $$ |  $$ |      $$ |  $$ |$$    $$ |$$ |  $$ |$$    $$ |$$ |  $$/ /    $$ |  $$ | __ $$ |  $$ |$$ |  $$/ 
$$ |__$$ |/$$$$$$$ | $$$$$$  |$$$$$$  |$$ \_$$ \_$$ |$$ \__$$ |$$ |      $$ \__$$ |      $$ \__$$ |$$$$$$$$/ $$ |  $$ |$$$$$$$$/ $$ |     /$$$$$$$ |  $$ |/  |$$ \__$$ |$$ |      
$$    $$/ $$    $$ |/     $$//     $$/ $$   $$   $$/ $$    $$/ $$ |      $$    $$ |      $$    $$ |$$       |$$ |  $$ |$$       |$$ |     $$    $$ |  $$  $$/ $$    $$/ $$ |      
$$$$$$$/   $$$$$$$/ $$$$$$$/ $$$$$$$/   $$$$$/$$$$/   $$$$$$/  $$/        $$$$$$$/        $$$$$$$ | $$$$$$$/ $$/   $$/  $$$$$$$/ $$/       $$$$$$$/    $$$$/   $$$$$$/  $$/       
$$ |                                                                                     /  \__$$ |                                                                               
$$ |                                                                                     $$    $$/                                                                                
$$/                                                                                       $$$$$$/                                                                                 
                                                                                                                                                                                  
"""

# Function to generate a password based on user input
def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special):
    if length < 4:
        print("Password length should be at least 4 for better security.")
        return None

# Define the character pool based on user input
    character_pool = ""
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_numbers:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation
    
# Ensure there is at least one character type selected
    if not character_pool:
        print("No character types selected. Please choose at least one type.")
        return None

    # Generate the password
    password = random.sample(character_pool, length)

    # Ensure password contains at least one of each selected type
    if use_uppercase:
        password[random.randint(0, length-1)] = random.choice(string.ascii_uppercase)
    if use_lowercase:
        password[random.randint(0, length-1)] = random.choice(string.ascii_lowercase)
    if use_numbers:
        password[random.randint(0, length-1)] = random.choice(string.digits)
    if use_special:
        password[random.randint(0, length-1)] = random.choice(string.punctuation)

# Shuffle pasword to avoid predictable patterns
    random.shuffle(password)
    return ''.join(password)

# Main function to run the password generator
def main():
    while True:
        print(password_gen_text)
        
        # Get user input for password criteria
        try:
            length = int(input("Enter password length (minimum 4): ").strip())
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
        
        # Generate password
        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special)
        
        # Display generated password if successful
        if password:
            print(f"Generated Password: {password}")
        
        # Check if user wants to generate another password
        another = input("Generate another password? (y/n): ").strip().lower()
        if another != 'y':
            print("Exiting Password Generator. Goodbye!")
            break

# Run the password generator
main()
