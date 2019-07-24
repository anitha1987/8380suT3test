import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class testEnroll(unittest.TestCase):

        def setUp(self):
                self.driver = webdriver.Chrome("C:/Users/Anitha/EducaTest/venv/Scripts/chromedriver.exe")

        def test_blog(self):
                driver = self.driver
                driver.maximize_window()

                driver.get("http://127.0.0.1:8000/")
                time.sleep(3)
                elem = driver.find_element_by_xpath("//*[@id=\"header\"]/ul/li[1]/a")
                elem.click()
                time.sleep(3)
                elem = driver.find_element_by_id("id_username")
                elem.send_keys("anitha")
                elem = driver.find_element_by_id("id_password")
                elem.send_keys("anitha")
                time.sleep(3)
                elem = driver.find_element_by_xpath("// *[ @ id = \"content\"] / div / div / form / p[3] / input")
                elem.click()
                time.sleep(3)
                elem = driver.find_element_by_xpath("//*[@id=\"content\"]/div[2]/h3/a")
                elem.click()
                time.sleep(3)
                elem = driver.find_element_by_xpath("//*[@id=\"content\"]/div/form/input[3]")
                elem.click()
                time.sleep(3)


        def tearDown(self):
                self.driver.close()


if __name__ == "__main__":
    unittest.main()