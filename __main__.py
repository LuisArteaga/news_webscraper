import ntpath
from selenium import webdriver as webdriver
from selenium.webdriver.common.by import By
import re

class Configuration:
    def __init__(self, driver='./driver/chromedriver.exe'):
        self.driver = ntpath.normpath(driver)


configuration = Configuration()
URL = 'https://www.finanzen.net/news/de/adidas-news@intpagenr_13'
driver = configuration.driver
driver = webdriver.Chrome(executable_path=driver)
driver.get(URL)

table_news = driver.find_element(By.XPATH, "//table[@class='table news-list']")
tr = table_news.find_elements(By.XPATH, '//tr')
re_date = r'[0-9]{2}\.[0-9]{2}\.[0-9]{2}\n'

for index, element in enumerate(tr):
    if re.match(re_date, element.text):
        print(repr(element.text).splitlines())




# <table class="table news-list">
# ->    <tbody>
# -->   <tr> (1)
# --->  <td> (1.1)
# ----> <div> (1.1.1) DATE
# --->  <td> (1.3)
# ----> <a class="teaser" ...> Titel

# --> <tr> (?)
# ---> <td colspan="3"> (?.1)
# ----> <span class="teaser-headline">
# -----> <a href="...">Title </a>
# Date fehlt


