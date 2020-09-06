from user import User
import string
import random
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
    def 