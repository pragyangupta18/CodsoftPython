contacts = []

def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email: ")
    address = input("Enter the address: ")

    contact = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Address": address,
    }
    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("Contact list is empty.")
    else:
        print("Contact List:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact['Name']}, Phone: {contact['Phone']}")

def search_contact():
    search_term = input("Enter the name or phone number to search: ")
    found_contacts = []

    for contact in contacts:
        if (
                search_term.lower() in contact['Name'].lower() or
                search_term in contact['Phone']
        ):
            found_contacts.append(contact)

    if found_contacts:
        print("Search results:")
        for i, contact in enumerate(found_contacts, start=1):
            print(f"{i}. Name: {contact['Name']}, Phone: {contact['Phone']}")
    else:
        print("No matching contacts found.")

def update_contact():
    search_term = input("Enter the name or phone number of the contact to update: ")
    found_contact = None

    for contact in contacts:
        if (
                search_term.lower() in contact['Name'].lower() or
                search_term in contact['Phone']
        ):
            found_contact = contact
            break

    if found_contact:
        print("Current contact information:")
        print(f"Name: {found_contact['Name']}")
        print(f"Phone: {found_contact['Phone']}")
        print(f"Email: {found_contact['Email']}")
        print(f"Address: {found_contact['Address']}")

        found_contact['Name'] = input("Enter new name (press Enter to keep current): ") or found_contact['Name']
        found_contact['Phone'] = input("Enter new phone number (press Enter to keep current): ") or found_contact[
            'Phone']
        found_contact['Email'] = input("Enter new email (press Enter to keep current): ") or found_contact['Email']
        found_contact['Address'] = input("Enter new address (press Enter to keep current): ") or found_contact[
            'Address']

        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    search_term = input("Enter the name or phone number of the contact to delete: ")
    found_contact = None

    for contact in contacts:
        if (
                search_term.lower() in contact['Name'].lower() or
                search_term in contact['Phone']
        ):
            found_contact = contact
            break

    if found_contact:
        contacts.remove(found_contact)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\nContact Book Options:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting the Contact Book.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
