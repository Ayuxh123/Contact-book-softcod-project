#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#project for codsoft: contact book

class Contact:
    """Class to represent a contact."""
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email} | {self.address}"


class ContactBook:
    """Class to manage the contact book."""
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        """Add a new contact to the contact book."""
        self.contacts.append(contact)
        print(f"Contact '{contact.name}' added successfully.")

    def view_contacts(self):
        """Display all contacts in the contact book."""
        if not self.contacts:
            print("No contacts found.")
            return
        print("\nContact List:")
        for contact in self.contacts:
            print(contact)

    def search_contact(self, search_term):
        """Search for contacts by name or phone number."""
        found_contacts = [contact for contact in self.contacts if search_term in contact.name or search_term in contact.phone]
        if found_contacts:
            print("\nSearch Results:")
            for contact in found_contacts:
                print(contact)
        else:
            print("No contacts found matching your search.")

    def update_contact(self, name, new_contact):
        """Update an existing contact's details."""
        for index, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                self.contacts[index] = new_contact
                print(f"Contact '{name}' updated successfully.")
                return
        print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        """Delete a contact from the contact book."""
        for index, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                del self.contacts[index]
                print(f"Contact '{name}' deleted successfully.")
                return
        print(f"Contact '{name}' not found.")


def main():
    """Main function to run the contact book application."""
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            new_contact = Contact(name, phone, email, address)
            contact_book.update_contact(name, new_contact)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting the contact book. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

