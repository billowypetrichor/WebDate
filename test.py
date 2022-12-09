from selenium import webdriver
import sys

# we need for the server, port and context to have variables
# to treat all the cases when the override default is set to false
host = sys.argv[1]
port = sys.argv[2]
application = sys.argv[3]
address = "http://"+host+":"+port+"/"+application+"/quoteAndBuy.do";

browser = webdriver.PhantomJS()
# browser.set_window_size(1120, 550)

browser.get(address)
print browser.current_url
address = browser.current_url
browser.get(address+"&_eventId=displayFormDate")
assert browser.find_elements_by_id("formDateBean")
#print browser.find_elements_by_id("formDateBean")
day = browser.find_element_by_id("day").get_attribute("value")
month = browser.find_element_by_id("month").get_attribute("value")
year = browser.find_element_by_id("year").get_attribute("value")
print browser.current_url
print day + month + year
