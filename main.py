from selenium import webdriver

# set webdriver: here we use chrome
driver = webdriver.Chrome("/usr/local/bin/chromedriver")

# bring us to the target website
driver.get("https://anwesende.imp.fu-berlin.de/S98dd6ab130")

# can use explict wait 解決目標標籤尚未出現前，程式可能會會做不出來


fields = driver.find_elements_by_class_name("requiredField")
for field in fields:
    print(field.text)
#driver.quit()