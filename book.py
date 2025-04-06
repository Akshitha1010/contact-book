#class Contact:
def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

        def  _str_(self):
                return f"name:{self.name}\nphone:{self.phone}\nemail:{self.email}"

# contactbook:
def _init_(self):
    self  .contacts=[]

    def add_contact(self, name, phone, email):
        new_contact = Contact (name, phone, email)
        self.contacts.append(new_contact)
        print(f"{name} has been added to the contacts book.")

        def _view_contacts(self):
            if not self.contacts:
                print("No contacts found.")
            else:
                for contact in self.contacts:
                    print(contact)
                    def search_contact(self, name):
                        for contact in self.contacts:
                            if contact.name == name:
                                print(contact)
                                return
                        print(f"No contact found with the name {name}.")
def delete_contact(self, name):
    for contact in self.contacts:
        if contact.name == name:
            self.contacts.remove(contact)
            print(f"{name} has been removed from the contacts book.")
            return
    print(f"No contact found with the name {name}.")
    def update_contact(self, name, new_name=None, new_phone=None, new_email=None):
        for contact in self.contacts:
            if contact.name == name:
                if new_name:
                    contact.name = new_name
                if new_phone:
                    contact.phone = new_phone
                if new_email:
                    contact.email = new_email
                print(f"{name}'s contact information has been updated.")
                return
        print(f"No contact found with the name {name}.")
def save_contacts(self, filename):
    with open(filename, 'w') as file:
        for contact in self.contacts:
            file.write(f"{contact.name},{contact.phone},{contact.email}\n")
    print(f"Contacts have been saved to {filename}.")           


def display_contact(): 
    contact_book = ContactBook()
    print("name\nphone\nemail")
    for key in contact_book.contacts:
        print(f"{key.name}\n{key.phone}\n{key.email}")

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Save Contacts")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ") 
            email = input("Enter email: ")     
            contact_book.add_contact(name, phone, email)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            name = input("Enter name to search: ")
            contact_book.search_contact(name)
        elif choice == '4':
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)
        elif choice == '5':
            name = input("Enter name to update: ")
            new_name = input("Enter new name (leave blank to skip): ")
            new_phone = input("Enter new phone (leave blank to skip): ")
            new_email = input("Enter new email (leave blank to skip): ")
            contact_book.update_contact(name, new_name, new_phone, new_email)
        elif choice == '6':
            filename = input("Enter filename to save contacts: ")
            contact_book.save_contacts(filename)
            display_contact
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    display_contact()
