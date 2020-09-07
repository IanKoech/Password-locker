import pyperclip
from credentials  import Credentials
#Imported pyperclip to save user passwords
class User:
    """
    Class generates user an account instance
    """
    Users_list=[]
    def __init__(self,user_name,password):
        self.user_name=user_name
        self.password=password
    
    def save_user(self):
        """
        Method saves a new user in the Users list
        """
        User.Users_list.append(self)

    def delete_user(self):
        """
        Method below deletes a user from the Users list
        """
        User.Users_list.remove(self)

    #Method below searches for users by name and returns the user
    @classmethod
    def find_user(cls,name):
        for user in cls.Users_list:
            if user.user_name==name:
                return user

    @classmethod
    def save_password(cls,name):
        """
        Method saves users password depending on the user
        """
        person_password=Credentials.find_user(name)
        pyperclip.copy(person_password.password)

    @classmethod
    def user_exists(cls,name):
        """
        Method checks if the user is in the users list
         and returns a boolean
        """
        for user in cls.Users_list:
            if user.user_name==name:
                return True
        return False
    @classmethod
    def display_users(cls):
        """
        Method displays all the user in the Users list
        """
        return cls.Users_list

    @classmethod
    def log_in(cls,name,password):
        """
        Method checks the name and password and allows users to log in
        """
        for user in cls.Users_list:
            if user.user_name== name and user.password==password:
                return Credentials.Credentials_list