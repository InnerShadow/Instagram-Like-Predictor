from colorama import Fore

#Get user name or create .txt file with user name
def GetUserName():
    try:
        with open ("Data/UserName.txt", 'r') as f:
            username = f.readline()
    except Exception:
        username = input(Fore.LIGHTWHITE_EX + "Enter user name: ")
        with open ("Data/UserName.txt", 'w') as f:
            f.write(username)
    return username


#Get password or create .txt file with password
def GetPassword():
    try:
        with open ("Data/Password.txt", 'r') as f:
            password = f.readline()
    except Exception:
        password = input(Fore.LIGHTWHITE_EX + "Enter password: ")
        with open ("Data/Password.txt", 'w') as f:
            f.write(password)
    return password

