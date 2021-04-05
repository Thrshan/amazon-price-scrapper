# import urllib.request

links = []
with open('links', 'r') as links_file:
    for line in links_file:
        links.append(line.strip())
print(links)
# page = urllib.request.urlopen(links[0])
# print(page.read())
#Simple assignment

from selenium.webdriver import Chrome
driver = Chrome()
# executable_path='/path/to/chromedriver'


driver.get("https://selenium.dev")

driver.close()