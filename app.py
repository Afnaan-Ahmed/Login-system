def login():
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

def registration():
    username = input("Username: ")
    password = input("Password: ")

    if f"{username},{password}" in open("user_data.txt").read():
        print("Account already exists.")
        print("Use your username and password to login")
    else:
        file = open("user_data.txt", "a")
        file.write(username)
        file.write(",")
        file.write(password)
        file.write("\n")
        file.close()
        print("Account created, use the id and password to login.")
