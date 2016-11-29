from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
 
# Replace below path with the absolute path
# to chromedriver in your computer
driver = webdriver.Chrome('/home/saket/Downloads/chromedriver')
 
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
 
# Replace 'Friend's Name' with the name of your friend 
# or the name of a group 
target = '"Friend\'s Name"'
 
# Replace the below string with your own message
string = "Message sent using Python!!!"
 
arg = '//span[contains(@title,' + target + ')]'
group = wait.until(EC.presence_of_element_located((
    By.XPATH, arg)))
group.click()
inp = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
input = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
for i in range(100):
    input.send_keys(string + Keys.ENTER)
    time.sleep(1)
