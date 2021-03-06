import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def main():
    if sys.argc != 2:
        sys.exit("Usage : python main.py link time")
    link = sys.argv[1]
    time_to_class = sys.argv[2]

    time.sleep(60*60*time_to_class)
    browser_path = "C:\chromedriver"
    chrome_options = webdriver.ChromeOptions()        
    chrome_options.add_argument(browser_path)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(link)
    mute = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div/div[1]')
    camera = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]')
    join = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[1]/span/span')
    mute.click()
    camera.click()
    join.click()
if __name__ == "__main__":
    main()