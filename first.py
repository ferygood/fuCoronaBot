# This is the first version of fuBot
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# set webdriver: here we use chrome
driver = webdriver.Chrome("/usr/local/bin/chromedriver")

# bring us to the target website
driver.get("https://anwesende.imp.fu-berlin.de/S98dd6ab130")

# can use explict wait 解決目標標籤尚未出現前，程式可能會會做不出來

firstName = driver.find_element_by_name("givenname")
firstName.send_keys("Yao-Chung")

lastName = driver.find_element_by_name("familyname")
lastName.send_keys("Chen")

street = driver.find_element_by_name("street_and_number")
street.send_keys("Kaiser-Wilhelm-Str 128")

zipCode = driver.find_element_by_name("zipcode")
zipCode.send_keys("12247")

town = driver.find_element_by_name("town")
town.send_keys("Lankwitz")

phone = driver.find_element_by_name("phone")
phone.send_keys("+49015252435228")

email = driver.find_element_by_name("email")
email.send_keys("yaochung41@gmail.com")

status = Select(driver.find_element_by_name("status_3g"))
status.select_by_value("22")

present_end = driver.find_element_by_name("present_to_dt")
end_time = input("enter your leaving time: ")
present_end.send_keys(str(end_time))

# then submit the file
driver.find_element_by_name("submit").click()