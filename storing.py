# Contact class to store contact information
class Contact:
    def __init__(self, store_name, phone_number, email, address):
        self.store_name = store_name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.store_name} - {self.phone_number}"

# ContactManager class to manage contacts
class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, store_name, phone_number, email, address):
        new_contact = Contact(store_name, phone_number, email, address)
        self.contacts.append(new_contact)
        print(f"Contact added: {new_contact}")

    def view_contact_list(self):
        print("Contact List:")
        for contact in self.contacts:
            print(contact)

    def search_contact(self, query):
        results = [contact for contact in self.contacts if query in contact.store_name or query in contact.phone_number]
        print("Search Results:")
        for contact in results:
            print(contact)

    def update_contact(self, store_name, phone_number, email, address):
        for contact in self.contacts:
            if contact.store_name == store_name:
                contact.phone_number = phone_number
                contact.email = email
                contact.address = address
                print(f"Contact updated: {contact}")
                return
        print("Contact not found")

    def delete_contact(self, store_name):
        for contact in self.contacts:
            if contact.store_name == store_name:
                self.contacts.remove(contact)
                print(f"Contact deleted: {contact}")
                return
        print("Contact not found")

# Main program
def main():
    contact_manager = ContactManager()

    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            store_name = input("Enter store name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_manager.add_contact(store_name, phone_number, email, address)

        elif choice == "2":
            contact_manager.view_contact_list()

        elif choice == "3":
            query = input("Enter search query: ")
            contact_manager.search_contact(query)

        elif choice == "4":
            store_name = input("Enter store name: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contact_manager.update_contact(store_name, phone_number, email, address)

        elif choice == "5":
            store_name = input("Enter store name: ")
            contact_manager.delete_contact(store_name)

        elif choice == "6":
            break

        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()