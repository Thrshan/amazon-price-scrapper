from selenium.webdriver import Chrome
from selenium import webdriver
from datetime import datetime
import sql_handler
import os

cwd = os.path.dirname(os.path.realpath(__file__))

def scrub(table_name):
    return ''.join( chr for chr in table_name if chr.isalnum() )

links = []
with open(cwd + '/links', 'r') as links_file:
    for line in links_file:
        links.append(line.strip())

dt = datetime.now()
ts = dt.timestamp()
date = dt.strftime("%Y-%m-%d %H:%M:%S")


try:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1420,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = Chrome(chrome_options=chrome_options)
    driver.get(links[0])
    title = driver.find_element_by_css_selector("#productTitle").text
    price = driver.find_element_by_css_selector(".offer-price").text

    db_file = cwd + '/db/price_list.db'
    data = {
        'date':date,
        'ts':ts,
        'price':float(price.split(' ')[-1])
    }
    sql_handler.insert_data_db(db_file, '"{}"'.format(title), data)
    print(data)
finally:
    driver.quit()

