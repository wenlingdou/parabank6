# Here is the main code module
import unittest
import parabank as pb

class ParabankpositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_register_account():
        pb.setUp()
        pb.register()
        pb.logout()
        pb.login()
        pb.logout()
        pb.tearDown()

####
