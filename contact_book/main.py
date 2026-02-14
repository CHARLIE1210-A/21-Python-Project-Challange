import json
import os

# ================= CONFIGURATION =================
DATA_FILE = 'contacts.json'


# ================= DATA HANDLING =================
def load_contacts():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as file:
        return json.load(file)
    
def save_contacts(contacts):
    with open(DATA_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)
       
       
# ================= VALIDATION ================= 
def validate_number(phone_number):
    return phone_number.isdigit() and len(phone_number) in [10, 11]


# ================= CRUD OPERATION =================
def add_contact(name, phone_number, email, contacts):
    contact = {
        'name': name,
        'phone_number': phone_number,
        'email': email,
    }
    contacts.append(contact)
    
def find_contact(contacts, keyword):
    keyword = keyword.lower()
    return [c for c in contacts if keyword in c['name'].lower() or keyword in c['phone_number'] or keyword in c['email']]

def update_contact(contacts, index, name=None, phone_number=None, email=None):
    if 0 <=  index < len(contacts):
        if name:
            contacts[index]['name'] = name
        if phone_number:
            contacts[index]['phone_number'] = phone_number
        if email:
            contacts[index]['email'] = email
        return True
    return False
    
def delete_contact(contacts, index):
    if 0 <= index < len(contacts):
        contacts.pop(index)
        return True
    return False


# ================= DISPLAY =================
def show_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return 
    
    for i, contact in enumerate(contacts):
                print(f"{i + 1}. {contact['name']} | 📞 {contact['phone_number']} | ✉️ {contact['email']}")


# ================= MENU =================
def show_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit\n")
    

# ================= MAIN APP =================
def main():
    contacts = load_contacts()
    
    while True:
        show_menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            
            if not validate_number(phone_number):
                print("Invalid phone number. It should contain only digits and be 10 or 11 digit long.\n")
                
            add_contact(name, phone_number, email, contacts)
            save_contacts(contacts)
            print("Contact added successfully.\n")

        elif choice == '2':
            show_contacts(contacts)
            
        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            results = find_contact(contacts, keyword)
            show_contacts(results)
            
        elif choice == '4':
            show_contacts(contacts)
            index = int(input("Enter contact number to update: ")) - 1
            name = input("Enter new name (leave blank to keep current): ")
            phone_number = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            
            if phone_number and not validate_number(phone_number):
                print("Invalid phone number. It should contain only digits and be 10 and 11 digit long.\n")
                continue
            
            if update_contact(contacts, index, name, phone_number, email):
                save_contacts(contacts)
                print("Contact updated successfully..\n")
            else:
                print("Invalid contact number.\n")
            
        elif choice == '5':
            show_contacts(contacts)
            index = int(input("Enter contact number to delete:")) - 1
            
            if delete_contact(contacts, index):
                save_contacts(contacts)
                print("Contact deleted successfully.\n")
                
            else:
                print("Invalid contact number.\n")

        elif choice == '6':
            print("Existing the program. Goodbye !!")
            break
        
        else:
            print("Invalid choice. Please try again.\n")
            
# ================= MAIN =================            
if __name__ == '__main__':
    main()
                