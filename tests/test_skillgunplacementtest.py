from selenium import webdriver
import time

driver = webdriver.Chrome()

#testcase 1 for login the testcases
def test_skillgun_login():
    driver.get("http://www.skillgun.com")
    mobile = driver.find_element('id', 'ContentPlaceHolder1_tbPhoneNumber')  # finding the webelement through id locator
    mobile.send_keys('9791639460')  # giving automation test case to give mobile number
    time.sleep(5)  # 5seconds to load the keys and entered values
    # to check email
    email = driver.find_element('id', 'ContentPlaceHolder1_tbEmail')  # same as mobile
    email.send_keys('bhaseerath7866@gmail.com')
    time.sleep(5)
    # to check password
    password = driver.find_element('id', 'ContentPlaceHolder1_tbPassword')  # same as mobile and email
    password.send_keys('bhasee@pilot#7866')
    time.sleep(5)
    # to tick checkbox
    checkbox = driver.find_element('id', 'ckbkPolicyAgreement')  # now we need  to tick the checkbox
    checkbox.click()  # clicking checkbox
    time.sleep(10)
    # to have login button
    # betweeen cekbox and login we have captcha in which selenium will not do captcha so give mannually
    login = driver.find_element('id', 'ContentPlaceHolder1_btnLogin')  # clicking login button
    login.click()
    time.sleep(5)

def test_skillgun_placementtest():
    newdrive = driver.find_element('id', 'ContentPlaceHolder1_ahrefnewdrive')  # clicking login button
    newdrive.click()
    time.sleep(5)

    back_home = driver.find_element('xpath','//*[@id="content"]/div[1]/div[1]/div/div/div/div/div[2]/fieldset/div[2]/div/a')  # clicking login button
    back_home.click()
    time.sleep(5)
