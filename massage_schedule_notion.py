from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pyvirtualdisplay import Display
import datetime

PATH = "/home/yl18410/chromedriver.exe"
options = webdriver.ChromeOptions()
DISPLAY_VISIBLE=0
DISPLAY_WIDTH = 400
DISPLAY_HEIGHT =1000
display = Display(visible=DISPLAY_VISIBLE, size =(DISPLAY_WIDTH, DISPLAY_HEIGHT))

#options.add_argument("--start-maximized")
driver = webdriver.Chrome(PATH, chrome_options=options)
action = ActionChains(driver)
time.sleep(1)


# Sign-in
driver.get('https://www.notion.so/Hair-massage-b8e81ad63c3e4c34bd68a2e14675b62a')
time.sleep(7)