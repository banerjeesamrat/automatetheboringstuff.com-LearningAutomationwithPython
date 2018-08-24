from selenium import webdriver

browser=webdriver.Firefox()
browser.get('https://inventwithpython.com')
try:
    elem=browser.find_element_by_class_name('bookcover')
    print('Found <%s> element with that class name!'%(elem.tag_name))
except:
    print('Was not able to find an element by that name.')
