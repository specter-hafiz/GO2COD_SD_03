#function to convert temperature from celsius to fahrenheit
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return round((celsius * 9/5) + 32, 2)

#function to convert temperature from fahrenheit to celsius
def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return round((fahrenheit - 32) * 5/9, 2)

#function to get valid temperature input
    """Prompt user for a valid numeric temperature input"""
def get_valid_temperature(prompt):
    """Prompt user for a valid numeric temperature input"""
    while True:
        try:
            temp = float(input(prompt))
            return temp
        except ValueError:
            print("Invalid input! Please enter a valid temperature value.")
   
#function to convert temperature
def convert_temperature():
    """Main function to handle temperature conversion"""
#while loop to keep the temperature converter running
while True:
#Prints the temperature conversion options
    print("\nTemperature Conversion Options:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

#Prompts the user to choose a conversion option
    try:
        choice = float(input("Choose a conversion option (1-3): "))
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
    else:
        if choice == 1:
            temp = get_valid_temperature("Enter temperature in Celsius: ")
            print(f"{temp}°C = {celsius_to_fahrenheit(temp)}°F")
        elif choice == 2:
            temp = get_valid_temperature("Enter temperature in Fahrenheit: ")
            print(f"{temp}°F = {fahrenheit_to_celsius(temp)}°C")
    # checks whether user wants to exit the program
        elif choice == 3:
            print("Exiting the program.")
            break
    # If the user chooses an invalid option, the program will print an error message
        else:
            print("Invalid option.")
    #Prompts the user if they would like to do another conversion after the conversion is done
        repeat = input("Would you like to do another conversion? (yes/no): ").lower()
        if repeat != 'yes' and repeat != 'y':
            print("Thank you for using the temperature converter. Goodbye!")
            break

#convert temperature function
convert_temperature()
