import sys

# Global list to store contacts. Each contact is a dictionary.
contacts = []

def add_contact(name, phone):
    """
    Adds a new contact to the global list.
    Args:
        name (str): The name of the contact.
        phone (str): The phone number of the contact.
    """
    # Create a dictionary for the new contact
    new_contact = {
        "name": name,
        "phone": phone
    }
    # Append the dictionary to the list
    contacts.append(new_contact)
    print(f"Contact '{name}' added successfully.")

def delete_contact(name):
    """
    Deletes a contact by name.
    Args:
        name (str): The name of the contact to delete.
    """
    global contacts
    # List comprehension to keep only contacts that do NOT match the name
    # This effectively deletes the contact(s) with the matching name
    initial_count = len(contacts)
    contacts = [c for c in contacts if c["name"].lower() != name.lower()]
    
    if len(contacts) < initial_count:
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

def view_contacts():
    """
    Displays all contacts sorted alphabetically by name.
    """
    if not contacts:
        print("No contacts found.")
        return

    # Sort the list of dictionaries by the 'name' key
    # We use a lambda function as the key for sorting
    sorted_contacts = sorted(contacts, key=lambda x: x["name"].lower())

    print("\n--- Contact List (Sorted) ---")
    for contact in sorted_contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}")
    print("-----------------------------")

def search_contact(name):
    """
    Searches for a contact by name using linear search.
    Args:
        name (str): The name to search for.
    """
    found = False
    print(f"\nSearching for '{name}'...")
    # Linear search: iterate through each contact in the list
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(f"Found: Name: {contact['name']}, Phone: {contact['phone']}")
            found = True
            # We don't break here in case there are multiple contacts with the same name,
            # though typically names might be unique. For this simple version, we show all matches.
    
    if not found:
        print(f"Contact '{name}' not found.")

def print_menu():
    print("\n=== Simple Contact Book Manager ===")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. View Contacts (Sorted)")
    print("4. Search Contact")
    print("5. Exit")
    print("===================================")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            name = input("Enter Name: ").strip()
            phone = input("Enter Phone Number: ").strip()
            if name and phone:
                add_contact(name, phone)
            else:
                print("Name and Phone cannot be empty.")
        elif choice == '2':
            name = input("Enter Name to delete: ").strip()
            if name:
                delete_contact(name)
            else:
                print("Name cannot be empty.")
        elif choice == '3':
            view_contacts()
        elif choice == '4':
            name = input("Enter Name to search: ").strip()
            if name:
                search_contact(name)
            else:
                print("Name cannot be empty.")
        elif choice == '5':
            print("Exiting Contact Book Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
