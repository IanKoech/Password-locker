class User :
    """
    Class generates user an account instance
    """
    Users_list=[]
    def _init_(self,user_name,password):
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