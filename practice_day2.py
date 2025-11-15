username = "Varghese"
password = "12345"

enter_username = input("Enter username: ")
enter_password = input("Enter password: ")

if enter_username == username and enter_password == password:
    print("Welcome Varghese! Login Successful")
else:
    print("Login Failed. Try Again")
