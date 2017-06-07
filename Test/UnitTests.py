import unittest
from Model.User import *


class TestMethods(unittest.TestCase):
    def authenticateAdmin(self):
        self.assertTrue(User.authenticate("vashanin7@gmail.com", "1111"))

    def getAdminInfo(self):
        admin = (1, u'vashanin7@gmail.com', u'1111', u'Vlad', u'Shanin', u'admin')
        self.assertEqual(User.getUserByEmail("vashanin7@gmail.com"), admin)


if __name__ == "__main__":
    unittest.main()