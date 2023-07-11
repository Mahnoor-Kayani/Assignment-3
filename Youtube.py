from selenium import webdriver

# Launch the browser and open the website
driver = webdriver.Chrome()
driver.get("https://www.youtube.com")

# Find and test the first element using find_element_by_id
element1 = driver.find_element_by_id("element1_id")
assert element1.is_displayed() and element1.is_enabled(), "Element 1 is not visible or enabled"

# Find and test the second element using find_element_by_name
element2 = driver.find_element_by_name("element2_name")
assert element2.is_displayed() and element2.is_enabled(), "Element 2 is not visible or enabled"

# Find and test the third element using find_element_by_xpath
element3 = driver.find_element_by_xpath("//input[@class='element3_class']")
assert element3.is_displayed() and element3.is_enabled(), "Element 3 is not visible or enabled"

# Find and test the fourth element using find_element_by_css_selector
element4 = driver.find_element_by_css_selector(".element4_selector")
assert element4.is_displayed() and element4.is_enabled(), "Element 4 is not visible or enabled"

# Close the browser
driver.quit()
