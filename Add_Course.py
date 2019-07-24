import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class testCourse(unittest.TestCase):

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

        # Add Course

        elem = driver.find_element_by_xpath("//*[@id=\"content-main\"]/div[2]/table/tbody/tr[1]/td[1]/a")
        elem.click()
        time.sleep(2)



        elem = driver.find_element_by_id("id_owner")
        elem.send_keys("James")
        time.sleep(1)
        elem = driver.find_element_by_id("id_subject")
        elem.send_keys("Biology")
        time.sleep(1)
        elem = driver.find_element_by_id("id_title")
        elem.send_keys("Botany")
        time.sleep(1)
        elem = driver.find_element_by_id("id_overview")
        elem.send_keys("Study of Plants and related topics ")
        time.sleep(1)
        elem = driver.find_element_by_id("id_modules-0-title")
        elem.send_keys("MB1")
        time.sleep(1)
        elem = driver.find_element_by_id("id_modules-0-description")
        elem.send_keys("Plant Taxonomy")
        time.sleep(1)
        elem = driver.find_element_by_id("id_modules-1-title")
        elem.send_keys("MB2")
        time.sleep(1)
        elem = driver.find_element_by_id("id_modules-1-description")
        elem.send_keys("Plant Morphology")
        time.sleep(1)
        elem = driver.find_element_by_id("id_modules-2-title")
        elem.send_keys("MB3")
        time.sleep(1)
        elem = driver.find_element_by_id("id_modules-2-description")
        elem.send_keys("Plant Physiology")
        time.sleep(1)
        elem = driver.find_element_by_xpath("// *[ @ id = \"course_form\"] / div / div[2] / input[1]")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id=\"user-tools\"]/a[1]")
        elem.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()




