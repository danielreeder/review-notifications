from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

browser_driver = Service(
    '/lib/chromium-browser/chromedriver'
)

options = Options()
#options.add_argument("--headless=new")

driver = webdriver.Chrome(service=browser_driver, options=options)
driver.get("https://www.tripadvisor.com/Hotel_Review-g51862-d2282005-Reviews-Inn_at_the_5th_Eugene-Eugene_Oregon.html")

sort_by = driver.find_element(By.CSS_SELECTOR, ".CkBUi.H")
sort_by.click()
print(sort_by.find_element(By.CSS_SELECTOR, "div:first-child").get_attribute("class"))

titles = driver.find_elements(By.CSS_SELECTOR, "div[data-test-target*='review-title']>a>span")
reviews = driver.find_elements(By.CSS_SELECTOR, "span[data-automation*='reviewText']>span")

for title, review in zip(titles, reviews):
    print(title.text)
    print(review.text)
    print('\n\n')

