import unittest
from credentials import Credentials
#Imported unittest module that allows running tests
#Imported the Credentials class to be used in our test cases

class TestCredentials(unittest.TestCase):
    """
    This class tests methods inside the Credentials class
    """
    def setUp(self):
        """
        Method runs before every test case
        """
        self.new_user=Credentials("Name","password")

    def tearDown(self):
        """
        Method makes the Credentials list empty
        """
        Credentials.Credentials_list=[]

    def test__init__(self):
        """
        Tests whether we can create instances of the class
        """
        self.assertEqual(self.new_user.user_name,"Name")
        self.assertEqual(self.new_user.password,"password")
    
    def test_save_credentials(self):
        """
        Method checks whether we can save a users credentials
        """
        self.new_user.save_credentials()
        self.assertEqual(len(Credentials.Credentials_list),1)
    
    def test_delete_credentials(self):
        """
        Method checks whether we can delete credentials from the list
        """
        self.new_user.save_credentials()
        other_user=Credentials("Person","123")
        other_user.save_credentials()
        other_user.delete_credentials()
        self.assertEqual(len(Credentials.Credentials_list),1)

    def test_generate_password(self):
        """
        Tests whether password generated has 7 figures
        """
        password_length=self.new_user.generate_password()
        self.assertEqual(len(password_length),7)

    def test_credentials_exist(self):
        """
        Tests the credential can be got
        """
        self.new_user.save_credentials()
        exists=self.new_user.credentials_exist("Name")
        self.assertTrue(exists)

    def test_display_credentials(self):
        """
        Tests whether the display credentials method works
        """
        self.assertEqual(Credentials.display_credentials(),Credentials.Credentials_list)
if __name__=="__main__":
    unittest.main()