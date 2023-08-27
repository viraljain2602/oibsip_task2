import json

# Load existing user data from file
try:
    with open('user_data.json', 'r') as file:
        user_database = json.load(file)
except FileNotFoundError:
    user_database = {}

def save_user_data():
    with open('user_data.json', 'w') as file:
        json.dump(user_database, file)

def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    user_database[username] = password
    save_user_data()
    print("Registration successful!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in user_database and user_database[username] == password:
        print("Login successful!")
        return True
    else:
        print("Login failed. Invalid username or password.")
        return False

def secured_page():
    print("Welcome to the secured page.")
    # Code for the secured page functionality goes here

def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            register()
        elif choice == "2":
            if login():
                secured_page()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
