from user import User
from credentials import Credentials
def create_user(name,password):
    """
    Function creates a user object
    """
    new_user=User(name,password)
    return new_user

def save_users(user):
    """
    Method saves users
    """
    user.save_user()

def delete_users(user):
    """
    Method deletes users
    """
    user.delete_user()

def find_users(name):
    """
    Returns the user
    """
    return User.find_user(name)

def user_log_in(name, password):
    '''
    Function that allows a user to log into their credential account
    Args:
        name : the name the user used to create their user account
        password : the password the user used to create their user account
    '''
    log_in = User.log_in(name, password)
    if log_in != False:
        return User.log_in(name, password)


def create_credential(user_password, name, password):
    '''
    Function to create a credential 
    Args:
        user_password : the password for Password Locker
        name : the name of the account 
        password : the password for the account
    '''

    new_credentials = Credentials(name,password)

    return new_credentails


def save_credentials(credential):
    '''
    Function to save a credential
    Args:
        credential : the credential to be saved
    '''

    credential.save_credentials()

def delete_credentials(credential):
    """
    Function to deletes a credential
    Args:
        credential : the credential to be deleted
    """
    credential.delete_credentials()

def check_existing_credentials(name):
    '''
    Function that checks if a user credential name already exists
    Args:
        name : the credential name
    '''

    return Credentials.credentials_exist(name)

def display_users():
    '''
    Function that returns all the saved users 
    '''

    return User.display_users()

def display_credentials(password):
    '''
    Function that returns all the saved credentials
    '''

    return Credentials.display_credentials(password)


def generated_password(name):
    '''
    Function that generates a password for the user 
    Args:
        name : the name of the account
    '''
    password = Credentials.generate_password()

    return password

def main():
    '''
    Function running the Password Locker app
    '''

    print("Password locker")

    while True:
        '''
        Loop that is running the entire application
        '''

        print('''   Short codes:
        cu - create a Password Locker account \n
        du - display names of current Password Locker users \n
        lg - log into your Password Locker account \n
        ex - exit the Password Locker account''')

        # Get short codes from the user
        short_code = input().lower()

        if short_code == 'cu':
            '''
            Creating a Password Locker account
            '''

            print("\n")
            print("New Password Locker Account")
            print("-"*10)

            print("User name ...")
            user_name = input()

            print("Password ...")
            password = input()

            # Create and saving new user
            save_users(create_user(user_name,password))
            #f string below
            print("\n")
            print(f"{user_name} welcome to Password Locker")
            print("\n")

        elif short_code == 'du':
            '''
            Display the names of the current users 
            '''

            if display_users():
                print("\n")
                print("Here are the current users of Password Locker")
                print("-"*10)

                for user in display_users():
                    print(f"{user.user_name}")
                    print("-"*10)
            else:
                print("\n")
                print("Password Locker has no current user.\n    Be our first user!!!")
                print("\n")

        elif short_code == 'lg':
            '''
            Logs in the user into their Password Locker account
            '''
            print("\n")
            print("Log into Password Locker Account")
            print("Enter the user name")
            user_name = input()

            print("Enter the password")
            password = input()

            if user_log_in(user_name,password) == None:
                print("\n")
                print("Please try again or create an account")
                print("\n")

            else:

                user_log_in(user_name,password)
                print("\n")
                print(f'''{user_name} welcome to your Credentials\n
                Use these short codes to get around''')

                while True:
                    '''
                    Loop to run functions after logging in,while loop lops till condition is met
                    '''
                    print('''  Short codes:
                    cc - add a credential \n
                    dc - display credentials \n
                    cg - create a credential with a generate password \n
                    ex - exit Credentials''')

                    # Get short code from the user
                    short_code = input().lower()

                    if short_code == 'cc':
                        '''
                        Creating a Credential
                        '''

                        print("\n")
                        print("New Credential")
                        print("-"*10)

                        print("Name of the credential ...")
                        credential_name = input()

                        print("Password of the credential ...")
                        credential_password = input()

                        # Create and save new user
                        save_credentials(create_credential(credential_name, credential_password))

                        print("\n")
                        print(f"Credentials for {credential_name} have been created and saved")
                        print("\n")

                    elif short_code == 'dc':
                        '''
                        Displaying credential name and password
                        '''

                        if display_credentials(password):
                            print("\n")
                            print(f"{user_name}\'s credentials")
                            print("-"*10)

                            for credential in display_credentials(password):
                                print(f"Account ..... {credential.credential_name}")
                                print(f"Password .... {credential.credential_password}")
                                print("-"*10)

                        else:
                            print("\n")
                            print("You have no credentials")
                            print("\n")

                    elif short_code == 'cg':
                        '''
                        Creating a credential with a generated password
                        '''

                        print("\n")
                        print("New Credential")
                        print("-"*10)

                        print("Name of the credential ...")
                        credential_name = input()

                        # Save new credential with its generated password
                        save_credentials( Credential(user_password, credential_name, (create_generated_password(credential_name)) ) )
                        print("\n")
                        print(f"Credentials for {credential_name} have been created and saved")
                        print("\n")

                    elif short_code == 'ex':
                        print(f"See you later {user_name}")
                        print("\n")
                        break

                    else:
                        print("\n")
                        print(f'''{short_code} does not compute.
    Please use the short codes''')
                        print("\n")

        elif short_code == 'ex':
            '''
            Exit Password Locker
            '''
            print("\n")
            print("Bye .....")

            break

        else:
            print("\n")
            print(f'''Come again, what's {short_code}?
    Please use the short codes''')
            print("\n")

if __name__=="__main__":
    main()