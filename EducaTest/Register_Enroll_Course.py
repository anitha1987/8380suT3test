import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class testRegister(unittest.TestCase):

    def setUp(self):
       self.driver = webdriver.Chrome("C:/Users/Anitha/EducaTest/venv/Scripts/chromedriver.exe")


    def test_blog(self):
        driver = self.driver
        driver.maximize_window()

        driver.get("http://127.0.0.1:8000/")

        elem = driver.find_element_by_xpath("//*[@id=\"content\"]/div[2]/h3/a")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id=\"content\"]/div/a")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("Karthikeyan")
        time.sleep(2)
        elem = driver.find_element_by_id("id_password1")
        elem.send_keys("Kart_123")
        time.sleep(2)
        elem = driver.find_element_by_id("id_password2")
        elem.send_keys("Kart_123")
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id=\"content\"]/div/form/p[5]/input")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id=\"content\"]/div/p/a")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id=\"content\"]/div[2]/h3/a")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id=\"content\"]/div/form/input[3]")
        elem.click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
