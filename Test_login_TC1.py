"""Passing valid email and password
 TC_01_LOGIN 
 Refer to  https://sampletestcases.com/test-cases-for-fb-login-page/ """

from packages.logger import project_logger
from packages.testsuites.suite_login.init import (
    TestData, SetUp, TearDown, setup_selenium_driver, unittest)

logger = project_logger("Login Test Case 1")

class test_01_login(unittest.Testcase):
    """Passing valid email and password"""
    
    def setUp(self):
        """called before every test"""
        self.driver = setup_selenium_driver()
        SetUp(self, self.driver)
        self.testdata = TestData()
        logger.info("setting up the test")
    
    def test_01(self):
        """Passing valid email and password"""
        self.email.send_keys(  # pylint: disable=no-member
            self.testdata.EMAIL_VALID)
        self.password.send_keys(  # pylint: disable=no-member
            self.testdata.PASSWORD_VALID)
        self.login.click()  # pylint: disable=no-member
        self.assertTrue(self.classifier.find_text_field_matching_label(# pylint: disable=no-member
                "login").is_displayed(), "Login button is not displayed")
    
    def tearDown(self):
        """called after every test"""
        TearDown(self.driver)

    
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_01_login))
    runner = unittest.TextTestRunner
    runner.run(suite)