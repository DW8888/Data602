contacts = {
    "Dazen Guile": "Dguile@brentweeks.com",
    "IronFist": "BlueFist@balckguard.gov",
    "Kip Guile": "SoNotTheLightBringer@turtlebear.io"
    
}

def lookup_email():
    name = input("Enter the name to look up: ")
    if name in contacts:
        print(f"The email address for {name} is {contacts[name]}")
    else:
        print(f"{name} not found in contacts.")
        return

def add_contact():
    name = input("Enter the name to add: ")
    if name in contacts:
        print(f"{name} already exists in contacts.")
        return
    else:
        email = input("Enter the email address: ")
        contacts[name] = email
        print(f"{name} added to contacts.")
        return

def change_email():
    name = input("Enter the name whose email you want to change: ")
    if name in contacts:
        new_email = input(f"Enter the new email address for {name}: ")
        contacts[name] = new_email
        print(f"The email address for {name} has been updated.")
        return
    else:
        print(f"{name} not found in contacts.")
        return

def delete_contact():
    name = input("Enter the name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"{name} has been deleted from contacts.")
        return
    else:
        print(f"{name} not found in contacts.")
        return


def menu():
    while True:
        print("\n---  The Chromeria Contact Management App  ---")
        print("1. Find someone")
        print("2. Add Someone")
        print("3. Update")
        print("4. Remove")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            lookup_email()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            change_email()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please select a valid option.")


menu()