from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

date_posted = []  # List to store date of the product
describe = []  # List to store the description of the product
price = []  # List to store price of the product
location = []  # List to store rating of the product

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.olx.com.pk/cats_c138/q-cats")

content = driver.page_source
soup = BeautifulSoup(content, features="lxml")

for data in soup.findAll('div', attrs={'class': '_1075545d _96d4439a d059c029 _858a64cf'}):

    dates = data.find_all_next('span', attrs={'class': '_2e28a695'})
    descriptions = data.find_all_next('div', attrs={'class': 'ee2b0479'})
    prices = data.find_all_next('div', attrs={'class': '_52497c97'})
    locations = data.find_all_next('span', attrs={'class': '_424bf2a8'})

    for created in dates:
        date_posted.append(created.text)
    for praise in descriptions:
        describe.append(praise.text)
    for fees in prices:
        price.append(fees.text)
    for area in locations:
        location.append(area.text)

print(len(date_posted), len(describe), len(price), len(location))
final = pd.DataFrame({'Cat Description': describe, 'Price': price, 'Date_Posted': date_posted, 'Location': location})
final.to_csv('catto.csv', index=True, encoding='utf-8')
print("A file called catto.csv has been created.")
