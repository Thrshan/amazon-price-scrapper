from selenium.webdriver import Chrome
import datetime
import time


links = []
with open('links', 'r') as links_file:
    for line in links_file:
        links.append(line.strip())
print(links)



try:
    driver = Chrome()
    driver.get(links[0])
    title = driver.find_element_by_css_selector("#productTitle").text
    price = driver.find_element_by_css_selector(".offer-price").text
    print(title, price)
finally:
    driver.quit()
"""
import sqlite3
con = sqlite3.connect('db/example.db')
cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE stocks
               (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
"""