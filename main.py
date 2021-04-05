from selenium.webdriver import Chrome
from datetime import datetime
import sql_handler
import time

def scrub(table_name):
    return ''.join( chr for chr in table_name if chr.isalnum() )

links = []
with open('links', 'r') as links_file:
    for line in links_file:
        links.append(line.strip())

dt = datetime.now()
ts = dt.timestamp()
date = dt.strftime("%Y-%m-%d %H:%M:%S")


try:
    driver = Chrome()
    driver.get(links[0])
    title = driver.find_element_by_css_selector("#productTitle").text
    price = driver.find_element_by_css_selector(".offer-price").text

    db_file = "db/price_list.db"
    data = {
        'date':date,
        'ts':ts,
        'price':float(price.split(' ')[-1])
    }
    sql_handler.insert_data_db(db_file, '"{}"'.format(title), data)
finally:
    driver.quit()

