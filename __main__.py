import ntpath
from selenium import webdriver as webdriver

class Configuration:
    def __init__(self, driver='./driver/chromedriver.exe'):
        self.driver = ntpath.normpath(driver)


def call_website(driver):
    URL = 'https://www.finanzen.net/news/de/adidas-news@intpagenr_13'
    driver = webdriver.Chrome(executable_path=driver)
    driver.get(URL)

configuration = Configuration()
call_website(configuration.driver)


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


