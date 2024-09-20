import sys
from contact_manager.database import Session
from contact_manager.models import User, Contact, Group

def main():
    session = Session()
    
    while True:
        print("\n1. Register User")
        print("2. Login User")
        print("3. Add Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. List Contacts")
        print("7. Add Group")
        print("8. List Groups")
        print("9. Search Contacts")
        print("10. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            username = input("Enter username: ")
            if session.query(User).filter(User.username == username).first():
                print("Username already exists.")
            else:
                new_user = User(username=username)
                session.add(new_user)
                session.commit()
                print("User registered.")

        elif choice == '2':
            username = input("Enter username: ")
            user = session.query(User).filter(User.username == username).first()
            if user:
                print(f"Welcome back, {username}!")
            else:
                print("User not found.")

        elif choice == '3':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email (optional): ")
            new_contact = Contact(name=name, phone=phone, email=email, user=user)
            session.add(new_contact)
            session.commit()
            print("Contact added.")
        
        elif choice == '4':
            contact_id = int(input("Enter contact ID to update: "))
            contact = session.query(Contact).filter(Contact.id == contact_id).first()
            if contact:
                contact.name = input("Enter new name: ")
                contact.phone = input("Enter new phone: ")
                contact.email = input("Enter new email (optional): ")
                session.commit()
                print("Contact updated.")
            else:
                print("Contact not found.")
        
        elif choice == '5':
            contact_id = int(input("Enter contact ID to delete: "))
            contact = session.query(Contact).filter(Contact.id == contact_id).first()
            if contact:
                session.delete(contact)
                session.commit()
                print("Contact deleted.")
            else:
                print("Contact not found.")
        
        elif choice == '6':
            contacts = session.query(Contact).all()
            print("Contacts:")
            for contact in contacts:
                print(f"{contact.id}: {contact.name}, {contact.phone}, {contact.email}")
        
        elif choice == '7':
            group_name = input("Enter group name: ")
            new_group = Group(name=group_name)
            session.add(new_group)
            session.commit()
            print("Group added.")

        elif choice == '8':
            groups = session.query(Group).all()
            print("Groups:")
            for group in groups:
                print(f"{group.id}: {group.name}")

        elif choice == '9':
            search_term = input("Enter name or phone number to search: ")
            results = session.query(Contact).filter(
                (Contact.name.like(f'%{search_term}%')) | 
                (Contact.phone.like(f'%{search_term}%'))
            ).all()
            print("Search Results:")
            for contact in results:
                print(f"{contact.id}: {contact.name}, {contact.phone}, {contact.email}")

        elif choice == '10':
            break
        
        else:
            print("Invalid choice. Try again.")
    
    session.close()

if __name__ == "__main__":
    main()
