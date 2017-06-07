import unittest
from Model.User import *
from Model.Subject import *

class TestMethods(unittest.TestCase):
    def test_authenticate_admin(self):
        self.assertTrue(User.authenticate("vashanin7@gmail.com", "1111"))

    def test_get_admin_info(self):
        admin = (1, u'vashanin7@gmail.com', u'1111', u'Vlad', u'Shanin', u'admin')
        self.assertEqual(User.getUserByEmail("vashanin7@gmail.com"), admin)

    def test_editting(self):
        self.assertTrue(Subject.edit(1, "description", "imageURL"))

    def test_init_users_table(self):
        self.assertTrue(User.init_table())

if __name__ == "__main__":
    unittest.main()