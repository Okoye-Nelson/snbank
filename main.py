import random


def login_check():
    print("\nKindly enter your details below to log into the system")
    x = True
    if x is True:
        u_name = str(input("Username: "))
        p_word = str(input("Password: "))
        for line in open("staff.txt", "r").readlines():
            check = line.split(",")
            username = check[0]
            password = check[1]
            if u_name == username and p_word == password:
                print("\nHello, "+username)
                x = False
                break
        else:
            print("\nUser doesn't exist!!!")


def account_create():
    while True:
        try:
            account_input = int(input('''Press 1 to create new bank account
Press 2 to check your account details
Press 3 to log out of the system:
>>> '''))

            if account_input == 1:
                print("\nKindly fill in the required fields below:")
                accountname = input("Account name: ")
                openingbalance = input("Opening balance: $")
                accounttype = input("Account type: ")
                accountemail = input("Account email: ")
                accountnumber = str(random.randint(1000000000, 1999999999))
                print(f"\nThis is your account number - '{accountnumber}'")

                file = open("customer.txt", "a")
                file.write(accountname)
                file.write(", $")
                file.write(openingbalance)
                file.write(", ")
                file.write(accounttype)
                file.write(", ")
                file.write(accountemail)
                file.write(", ")
                file.write(accountnumber)
                file.write("\n")
                file.close()
                print("And your new account has been created and stored successfully!\n")

            if account_input == 2:
                while True:
                    try:
                        account_check = input("\nEnter your account number: \n")
                        file = open("customer.txt", "r")
                        for line in file.readlines():
                            check = line.split(",")
                            accountname = check[0]
                            openingbalance = check[1]
                            accounttype = check[2]
                            accountemail = check[3]
                            accountnumber = check[4]
                            if account_check == accountnumber:
                                print(f"Account name is {accountname}")
                                print(f"Opening balance is {openingbalance}")
                                print(f"Account Type is {accounttype}")
                                print(f"Account Email is {accountemail}")
                                file.close()
                                break
                        else:
                            print("\nYou provided an invalid account number\n")
                        break
                    except ValueError:
                        print("You should type in the specified number value\n")
                    except IndexError:
                        print()
            if account_input == 3:
                break
        except ValueError:
            print("Invalid input\n")


def login_confirmation():
    while True:
        try:
            print('''Hello there! welcome to HNG Bank
How can we be of service to you today?''')
            login_input = int(input("\nPress 1, for your Staff Login or Press 2, to end the service: "))
            while login_input <= 0 or login_input >= 3:
                try:
                    login_input = int(input("Kindly input either 1 and 2 as specified above: "))
                except TypeError:
                    pass
            if login_input == 1:
                login_check()
                account_create()
            else:
                if login_input == 2:
                    print("\nAlright, see you some other time. Bye!")
                    break
        except ValueError:
            print("\nSorry, you have typed in an unspecified value. Let us do this again.\n")


login_confirmation()
