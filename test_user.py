import unittest
from user import User

class TestUser(unittest.TestCase):
    """
    This class tests the methods inside the User class
    """
    def setUp(self):
        """
        Method runs  before all test cases that require checking the Users
        list
        """
        self.new_user=User("IanKoech","liveoutloud")

    def tearDown(self):
        """
        Tears down users list to have none
        """

        User.Users_list=[]
    
    def test_init(self):
        """
        Tests whether object is initialized correctly
        """
        self.assertEqual(self.new_user.user_name,"IanKoech")
        self.assertEqual(self.new_user.password,"liveoutloud")
    
    def test_save_user(self):
        """
        Method checks whether user entered is saved and checks the length of the Users list
        """
        #Line below saves the user to the list
        self.new_user.save_user()
        self.assertEqual(len(User.Users_list),1)

    def test_delete_user(self):
        """
        Tests if we can remove a user from User list
        """
        self.new_user.save_user()
        #Removing user below
        other_user=User("Name","1234")
        other_user.save_user()
        other_user.delete_user()
        self.assertEqual(len(User.Users_list),1)

    def test_find_user(self):
        """
        Method tests whether a user can be found by
        entering their name and returns their details
        """
        self.new_user.save_user()
        user_other=User("Kihara","1223344")
        user_other.save_user()
        #Saved new user above
        find_name=User.find_user("Kihara")
        #Below runs test to check if the names match
        self.assertEqual(find_name.user_name,user_other.user_name)

    def test_user_exists(self):
        """
        Test checks whether the a user can be found by their name and
        returns a boolean
        """
        self.new_user.save_user()
        user_other=User("Kihara","1124343")
        user_other.save_user()
        user_test=user_other.user_exists("Kihara")
        self.assertTrue(user_test)
        #We test above whether the user exists
        
    def test_display_users(self):
        """
        Method checks whether we can return all users
        """
        self.assertEqual(User.display_users(),User.Users_list)
    

if __name__=="__main__":
    unittest.main()
    #Runs to check tests 