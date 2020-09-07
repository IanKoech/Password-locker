import string
import random

#Imported pyperclip to save entered passwords
class Credentials:
    """
    Class instantiates user credentials
    """
    Credentials_list=[]
    def __init__(self,user_name,password):
        self.user_name=user_name
        self.password=password
    
    def save_credentials(self):
        """
        Method saves entered credentials into Credentials list
        """
        Credentials.Credentials_list.append(self)
    
    def delete_credentials(self):
        """
        Method deletes credentials from Credentials list when inoked
        """
        Credentials.Credentials_list.remove(self)
    
    @classmethod
    def generate_password(cls):
        "Method generates password of a given length depending on user input"
        #Length parameter determines the length of your password
        letters=string.ascii_lowercase
        #Generating a password of a particular length
        password="".join(random.choice(letters) for i in range(7))
        return password

    @classmethod 
    def credentials_exist(cls,name):
        """
        Method checks if a particular user
        has entered their credentials
        """
        for credentials in cls.Credentials_list:
            if credentials.user_name==name:
                return True
        return False
    
    
    @classmethod
    def display_credentials(cls):
        """
        Method returns the credentials list in the class
        """
        return cls.Credentials_list
if __name__=="__main__":
    unittest.main()
