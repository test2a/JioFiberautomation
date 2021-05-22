from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
f = open('ipv6address.txt', 'r')
content=f.read()
driver = webdriver.Chrome("chromedriver")
driver.get("http://192.168.29.1");



username_input ='//*[@id="tf1_userName"]'
password_input='//*[@id="tf1_password"]'
login_submit='/html/body/div[1]/div/div/div[2]/form/div/div[5]/button'
security='//*[@id="mainMenu4"]'
firewall='//*[@id="tf1_security_defaultPolicy"]'
ipv6firewall='//*[@id="main"]/div[6]/ul/li[3]/a'
rdlistitem='//*[@id="3"]'
edit3editem='//*[@id="editMenu"]'

ipv6inputmodal='//*[@id="tf1_dialog"]/div[2]'
ipv6submit='//*[@id="tf1_dialog"]/div[3]/input[2]'
exitdrop='//*[@id="main"]/div[1]/div[1]/p'
exitlogout='//*[@id="tf1_logoutAnchor"]'
exitconfirm='//*[@id="tf1_logOutContent"]/div/a[2]'
driver.find_element_by_xpath(username_input).send_keys('admin')
driver.find_element_by_xpath(password_input).send_keys('Password')
driver.find_element_by_xpath(login_submit).click()
time.sleep(8)
driver.find_element_by_xpath(security).click()
time.sleep(3)
driver.find_element_by_xpath(firewall).click()
time.sleep(6)
driver.find_element_by_xpath(ipv6firewall).click()
time.sleep(6)
driver.find_element_by_xpath(rdlistitem).click()
id3edit=driver.find_element_by_xpath('//*[@id="3"]')
ActionChains(driver).move_to_element(id3edit).context_click(id3edit).perform()

driver.find_element_by_xpath(edit3editem).click()
time.sleep(4)
#driver.find_element_by_xpath(ipv6inputmodal).click()

id3inputbox='/html/body/div[1]/div[2]/div[6]/div/form/div/div[2]/div[18]/input'
driver.find_element_by_xpath(id3inputbox).clear()
driver.find_element_by_xpath(id3inputbox).send_keys(content)
time.sleep(1)
driver.find_element_by_xpath(ipv6submit).click()
time.sleep(5)
driver.find_element_by_xpath(exitdrop).click()
driver.find_element_by_xpath(exitlogout).click()
time.sleep(1)
driver.find_element_by_xpath(exitconfirm).click()
