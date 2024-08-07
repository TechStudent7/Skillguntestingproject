from selenium import webdriver
import time
driver = webdriver.Chrome()
#login testcase 1
def test_skillgun_login():
    driver.get("http://www.skillgun.com")  # testing website url
    # to give mobile number
    mobile = driver.find_element('id', 'ContentPlaceHolder1_tbPhoneNumber')  # finding the webelement through id locator
    mobile.send_keys('your MobileNO here')  # giving automation test case to give mobile number
    time.sleep(5)  # 5seconds to load the keys and entered values
    # to check email
    email = driver.find_element('id', 'ContentPlaceHolder1_tbEmail')  # same as mobile
    email.send_keys('your MailID here')
    time.sleep(5)
    # to check password
    password = driver.find_element('id', 'ContentPlaceHolder1_tbPassword')  # same as mobile and email
    password.send_keys('your Password')
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

#testcase2 testing profile settings
def test_skillgun_profilesettings():
    profile = driver.find_element('link text', 'profile settings')
    profile.click()
    time.sleep(5)  # wait for few seconds too oprn profile page
    assert 'ProfileSetting' in driver.current_url

#testcase 3 testing if edit contacts button
def test_skillgun_profile_editcontacts():
    edit = driver.find_element('id', 'ContentPlaceHolder1_hlEditContact')
    edit.click()
    time.sleep(5)
    assert 'EditContact' in driver.current_url

#testcase4 to save the contact details working or not
def test_skillgun_profile_savecontacts():
    cur_add_line = driver.find_element('id', 'ContentPlaceHolder1_tbCALine1')
    cur_add_line.clear()
    cur_add_line.send_keys('krishnagiri')

    save = driver.find_element('id', 'ContentPlaceHolder1_btnSubmit')
    save.click()
    time.sleep(5)