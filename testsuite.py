from unittest import TestLoader, TestSuite, TextTestRunner


from Subject import testSubject
from Login_Logout import testLoginLogout
from Add_Course import testCourse
from Enroll_Course import testEnroll
from Register_Enroll_Course import testRegister




if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(testLoginLogout),
        loader.loadTestsFromTestCase(testSubject),
        loader.loadTestsFromTestCase(testCourse),
        loader.loadTestsFromTestCase(testEnroll),
        loader.loadTestsFromTestCase(testRegister),

    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)