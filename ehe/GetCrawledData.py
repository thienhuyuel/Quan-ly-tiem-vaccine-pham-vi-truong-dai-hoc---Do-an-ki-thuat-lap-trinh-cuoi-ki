"""
iframe css selector: #chartCovidStatistics > iframe
table xpath: /html/body/div[2]/div[1]/div
city
total
daynow
die
"""


from pkgutil import get_data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime


class Get():
    def __init__(self):
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        self.driver = webdriver.Chrome(options=option)

    def get_data(self):
        url = 'https://covid19.gov.vn/'
        self.driver.get(url)

        #iframe = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/iframe')
        self.driver.switch_to.frame(1)

        table = self.driver.find_elements_by_xpath('/html/body/div[2]/div[1]/div')
        for row in table:
            cites_ele = row.find_elements_by_class_name('city')
            total_ele = row.find_elements_by_class_name('total')
            total_day_ele = row.find_elements_by_class_name('daynow')
            deaths_ele = row.find_elements_by_class_name('die')

        cities = []
        total = []
        total_day = []
        death = []

        for i in range(len(cites_ele)):
            cities.append(cites_ele[i].text)
            total.append(total_ele[i].text)
            total_day.append(total_day_ele[i].text)
            death.append(deaths_ele[i].text)

        self.driver.close()

        return [cities,total,total_day,death]
    """
    def write_to_file(self):
        f = open('data.txt','a',encoding='utf-8')
        for i in self.get_data():
            for x in i:
                f.write(x + '\n')
        f.close()
    """
class Data():
    def __init__(self):
        g = Get()
        data = g.get_data()
        self.cities = data[0]
        self.total_cases = data[1]
        self.total_day = data[2]
        self.death = data[3]
        x = datetime.datetime.now()
        self.time = x.strftime("%d - %m - %Y\n%H:%M:%S.%f")
        
        

