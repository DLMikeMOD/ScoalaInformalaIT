from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

def browser_function():
    driver_path = "path/to/chromedriver"
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    chr_driver = webdriver.Chrome(driver_path, options=chr_options)
    chr_driver.get("https://www.emag.ro/#opensearch")

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.emag.ro/#opensearch")
get_element = browser.find_element(by=By.ID, value="searchboxTrigger")
get_element.send_keys('Razer')
get_element.submit()

search_element = browser.find_element(by=By.ID, value="card_grid")
# print(search_element.text)
search_element_title = browser.find_element(by=By.CLASS_NAME, value= "card-v2-title")
print(search_element_title.text)