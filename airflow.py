from selenium import webdriver
import time


driver =  webdriver.Chrome('..\driver\chromedriver.exe')

driver.get("http://127.0.0.1:4000/student")

driver.find_element_by_id("id_NAME").send_keys("Vedhika")
time.sleep(5)
driver.find_element_by_id("id_PLACE").send_keys("Wayanad")
time.sleep(5)
driver.find_element_by_xpath("/html/body/form/input[2]").click()
time.sleep(5)

driver.get("https://qm66558.ap-south-1.aws.snowflakecomputing.com/console")
time.sleep(5)
driver.find_element_by_id("base-textfield-1022-inputEl").send_keys("Aatmay")
time.sleep(5)
driver.find_element_by_id("password-id-inputEl").send_keys("Aagney@2016")
time.sleep(5)
driver.find_element_by_xpath("//*[@id='base-button-1025-btnEl']").click()
time.sleep(5)

btn=driver.find_element_by_xpath("//*[@id='sleet-component-1181']/div/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div[6]")
btn.send_keys("/n")
time.sleep(5)
driver.find_element_by_xpath("//*[@id='sleet-component-1181']/div/div/div[2]/div[2]/div[1]/div[1]/div/div[1]/div[2]/button").click()
time.sleep(5)
