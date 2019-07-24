import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class testSubject(unittest.TestCase):

    def setUp(self):
       self.driver = webdriver.Chrome("C:/Users/Anitha/EducaTest/venv/Scripts/chromedriver.exe")


    def test_blog(self):
        driver = self.driver
        driver.maximize_window()

        driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")

       # Login in Admin Page

        elem = driver.find_element_by_id("id_username")
        elem.send_keys("anitha")
        time.sleep(2)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("anitha")
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id=\"login-form\"]/div[3]/input")
        elem.click()
        time.sleep(2)

        # Add Subject

        elem = driver.find_element_by_xpath("// *[ @ id = \"content-main\"] / div[2] / table / tbody / tr[2] / td[1] / a")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_title")
        elem.send_keys("Mathematics")
        elem = driver.find_element_by_xpath("// *[ @ id = \"subject_form\"] / div / div / input[1]")
        elem.click()
        time.sleep(2)



        # Delete Subject

        #elem = driver.find_element_by_xpath("//*[@id=\"result_list\"]/tbody/tr[1]/th/a")
        #elem.click()
        #time.sleep(2)
        #elem = driver.find_element_by_xpath("//*[@id=\"subject_form\"]/div/div/p/a")
        #elem.click()
        #time.sleep(2)
        #elem = driver.find_element_by_xpath("// *[ @ id = \"content\"] / form / div / input[2]")
        #elem.click()
        #time.sleep(2)






    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


