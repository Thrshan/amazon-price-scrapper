from selenium.webdriver import Chrome
from selenium import webdriver
from datetime import datetime
import hjson
import sql_handler
import os

cwd = os.path.dirname(os.path.realpath(__file__))
import json

with open(cwd + '/config.hjson') as config_file:
    config = hjson.load(config_file)

def scrub(table_name):
    return ''.join( chr for chr in table_name if chr.isalnum() )

dt = datetime.now()
ts = dt.timestamp()
date = dt.strftime("%Y-%m-%d %H:%M:%S")


try:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1420,1080')
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = Chrome(chrome_options=chrome_options)
    for productLink in config['productLinks']:
        driver.get(productLink)
        title = driver.find_element_by_css_selector("#productTitle").text
        if len(driver.find_elements_by_css_selector(".offer-price")) > 0:
            price = driver.find_element_by_css_selector(".offer-price").text
        else:
            print(".offer-price not exist")
            price = driver.find_element_by_css_selector("#priceblock_ourprice").text

        print(price)
        price = price.replace("₹","").replace(",","")
        print(price)
        price = float(price.strip())
        print(price)

        db_file = cwd + '/db/' + config['dbFile'] if config['dbPath'] == "" else config['dbPath'] + "/" + config['dbFile']
        
        data = {
            'date':date,
            'ts':ts,
            'price':price
        }
        sql_handler.insert_data_db(db_file, '"{}"'.format(title), data)
        print(data)
finally:
    driver.quit()

