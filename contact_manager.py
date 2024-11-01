# Initialize an empty list to store contacts
contacts = []

contact_manager_text = """

 ######   #######  ##    ## ########    ###     ######  ########    ##     ##    ###    ##    ##    ###     ######   ######## ########  
##    ## ##     ## ###   ##    ##      ## ##   ##    ##    ##       ###   ###   ## ##   ###   ##   ## ##   ##    ##  ##       ##     ## 
##       ##     ## ####  ##    ##     ##   ##  ##          ##       #### ####  ##   ##  ####  ##  ##   ##  ##        ##       ##     ## 
##       ##     ## ## ## ##    ##    ##     ## ##          ##       ## ### ## ##     ## ## ## ## ##     ## ##   #### ######   ########  
##       ##     ## ##  ####    ##    ######### ##          ##       ##     ## ######### ##  #### ######### ##    ##  ##       ##   ##   
##    ## ##     ## ##   ###    ##    ##     ## ##    ##    ##       ##     ## ##     ## ##   ### ##     ## ##    ##  ##       ##    ##  
 ######   #######  ##    ##    ##    ##     ##  ######     ##       ##     ## ##     ## ##    ## ##     ##  ######   ######## ##     ## 

"""

#function to add a contact
def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    
    contacts.append(contact)
    print(f"Contact '{name}' added successfully.")

#function to view contacts in list of contacts
def view_contacts():
    if not contacts:
        print("No contacts to display.")
    else:
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

#function to search for a contact 
def search_contact():
    search_query = input("Enter name or phone number to search: ").strip()
    found_contacts = [c for c in contacts if c["name"] == search_query or c["phone"] == search_query]
    
    if found_contacts:
        for contact in found_contacts:
            print(f"Found - Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("No contact found with that information.")

#function to edit a contact
def edit_contact():
    name = input("Enter the name of the contact you want to edit: ").strip()
    for contact in contacts:
        if contact["name"] == name:
            print("Leave blank to keep current value.")
            new_name = input(f"Enter new name ({contact['name']}): ").strip() or contact["name"]
            new_phone = input(f"Enter new phone ({contact['phone']}): ").strip() or contact["phone"]
            new_email = input(f"Enter new email ({contact['email']}): ").strip() or contact["email"]
            
            contact.update({"name": new_name, "phone": new_phone, "email": new_email})
            print(f"Contact '{name}' updated successfully.")
            return
    print("Contact not found.")

#function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact you want to delete: ").strip()
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            print(f"Contact '{name}' deleted successfully.")
            return
    print("Contact not found.")

#function to display the main menu
def main_menu():
    while True:
        print(contact_manager_text+"\n")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            edit_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# Run the program
main_menu()
