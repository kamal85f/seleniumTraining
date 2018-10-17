from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

browser = webdriver.Chrome()
browser.get('http:\\google.com')
searchTextField = browser.find_element_by_id("lst-ib")
searchTextField.send_keys("python")
searchTextField.send_keys(Keys.RETURN)

browser.close() 




