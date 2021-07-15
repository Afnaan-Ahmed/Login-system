logged_in = False
given_username = input("Username: ")
given_password = input("Password: ")

with open("user_data.txt","r") as file:
    if f"{given_username},{given_password}" in file.read():
        logged_in = True
        print("logged in")
    else:
        logged_in = False
        print("Invalid username/password.")
        