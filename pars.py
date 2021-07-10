from config import DRIVER_PATH, URL
from selenium import webdriver
from time import sleep
from config import DRIVER_PATH, URL1

driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(URL)
sleep(10) 
weather = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[1]/div[5]/a/div[1]/span[2]')
weather1 = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[1]/div[5]/a/div[2]/div[1]')
weather2 = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[1]/div[5]/a/div[2]/div[2]')
print(weather.text)

driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(URL1)
sleep(10) 
kal = driver.find_element_by_xpath('//*[@id="right-sidebar"]/div/div/div[1]/div/div[1]/span')


def __del__(self):
    self.driver.close()