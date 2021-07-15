import urllib3
from bs4 import BeautifulSoup
import re

url = 'https://www.amazon.in/4-Hour-Work-Week-Escape-Anywhere/dp/0091929113'
url='https://www.amazon.in/dp/B08ZJSQGJZ/ref=s9_acss_bw_pg_test_9_i?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-16&pf_rd_r=ZFKTJC5GM9W0XYTB8Q1H&pf_rd_t=101&pf_rd_p=9c64821e-71c3-4d19-a943-d93fe012e8dc&pf_rd_i=1389401031'
url='https://www.amazon.in/Psychology-Money-Morgan-Housel/dp/9390166268/?_encoding=UTF8&pd_rd_w=U4UBT&pf_rd_p=934b3e70-b228-4995-99a9-9271c35f60a7&pf_rd_r=VE3V8TY1QCCQX5EHHR62&pd_rd_r=558b0497-75c9-46a4-91ee-b82a5f896776&pd_rd_wg=zKnFv&ref_=pd_gw_crs_wish'
url='https://www.amazon.in/dp/B07HHHTRQZ/?coliid=I1FZS5HZRCNRU6&colid=39WEU3EPLS3EQ&psc=0&ref_=lv_ov_lig_dp_it'
url='https://www.amazon.in/dp/B079P82D4C/?coliid=I1X89BY76YUPYY&colid=39WEU3EPLS3EQ&psc=1&ref_=lv_ov_lig_dp_it'
url='https://www.amazon.in/dp/B011UK5DGY/?coliid=I2VTBG3W7LVRB0&colid=39WEU3EPLS3EQ&psc=1&ref_=lv_ov_lig_dp_it'
url='https://www.amazon.in/dp/076117897X/?coliid=I2J0EB5JVRQ4CN&colid=1R6IKOF2U9AZC&psc=1&ref_=lv_ov_lig_dp_it'

http = urllib3.PoolManager()

r = http.request('GET', url)
# print(r.status)
html_doc = r.data
soup = BeautifulSoup(html_doc, 'html.parser')

product_title = soup.find(id='productTitle').string

if soup.find(id='priceblock_dealprice'):
    price_block = soup.find(id='priceblock_dealprice')
    price = price_block.string
elif soup.find(id='priceblock_ourprice'):
    price_block = soup.find(id='priceblock_ourprice')
    price = price_block.string
else:
    buy_block = soup.find(id='buybox')
    price_elem = soup.find_all(class_='offer-price')
    price = price_elem[0].string

price = re.sub('[^\d\.]', '', price)
price = float(price)
print(product_title)
print(price)