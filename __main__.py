import ntpath
from selenium import webdriver as webdriver
from selenium.webdriver.common.by import By
import re
import csv


class Configuration:
    """
    This class contains the information about the chrome driver and the details about website to be crawled
    """

    def __init__(self, chrome_driver='./driver/chromedriver.exe'):
        self.driver = ntpath.normpath(chrome_driver)
        self.websites = {'finanzen.net': {'stocks': ['adidas',
                                                     'allianz',
                                                     'beiersdorf',
                                                     'deutsche_bank',
                                                     'deutsche_telekom',
                                                     'lufthansa',
                                                     'siemens',
                                                     'volkswagen'
                                                     'vonovia',
                                                     'wirecard'
                                                     ],
                                          'base_url': 'https://www.finanzen.net/news/de/',
                                          'url_parameters': '-news@intpagenr_'}}


configuration = Configuration()
driver = configuration.driver
driver = webdriver.Chrome(executable_path=driver)

BASE_URL = configuration.websites['finanzen.net']['base_url']

for stock in configuration.websites['finanzen.net']['stocks']:
    url = BASE_URL + stock + configuration.websites['finanzen.net']['url_parameters']
    for i in range(1, 26):
        driver.get(url+str(i))
        driver.implicitly_wait(10)
        re_date = r'[0-9]{2}\.[0-9]{2}\.[0-9]{2}\n'
        table_news = driver.find_element(By.XPATH, "//table[@class='table news-list']")
        tr = table_news.find_elements(By.XPATH, '//tr')

        with open('./export/{}-{}.csv'.format(stock, str(i)), 'w', newline='') as file:
            writer = csv.writer(file)
            for index, element in enumerate(tr):
                if re.match(re_date, element.text):
                    writer.writerow(
                        re.sub(string=repr(element.text), pattern='(^\'|\'$|^"|"$)', repl='').split(sep='\\n'))
