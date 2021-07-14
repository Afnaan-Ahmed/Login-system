#this is just the registration of a user not the login system.
username = input("Username: ")
password = input("Password: ")

file = open("user_data.txt", "a")
file.write(username)
file.write(",")
file.write(password)
file.write("\n")
file.close()

print("Account created, use the id and password to login.")
