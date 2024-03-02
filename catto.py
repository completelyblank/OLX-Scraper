import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Your Chrome version:
chrome_version = "122.0.6261.69"

# Define the lists outside the function
date_posted = []
describe = []
price = []
location = []

def scrape_data():
    # Use global keyword to access global variables
    global date_posted, describe, price, location

    date_posted.clear()
    describe.clear()
    price.clear()
    location.clear()

    chrome_options = Options()
    # chrome_options.add_argument('--headless')  # Add this line if you don't want to open a visible browser window

    # Specify ChromeDriver version
    chrome_driver_version = f"{chrome_version}.0"
    driver = webdriver.Chrome(ChromeDriverManager(version=chrome_driver_version).install(), options=chrome_options)
    driver.get("https://www.olx.com.pk/cats_c138/q-cats")

    content = driver.page_source
    soup = BeautifulSoup(content, features="lxml")

    for data in soup.findAll('div', attrs={'class': '_1075545d _96d4439a d059c029 _858a64cf'}):
        dates = data.find_all_next('span', attrs={'class': '_2e28a695'})
        descriptions = data.find_all_next('div', attrs={'class': 'ee2b0479'})
        prices = data.find_all_next('div', attrs={'class': '_52497c97'})
        locations = data.find_all_next('span', attrs={'class': '_424bf2a8'})

        for created, praise, fees, area in zip(dates, descriptions, prices, locations):
            date_posted.append(created.text)
            describe.append(praise.text)
            price.append(fees.text)
            location.append(area.text)

    driver.quit()

    update_gui()

def update_gui():
    tree.delete(*tree.get_children())
    for i, (date, desc, pr, loc) in enumerate(zip(date_posted, describe, price, location), 1):
        tree.insert("", "end", values=(i, date, desc, pr, loc))

# Create the main window
root = tk.Tk()
root.title("OLX Cat Scraping App")

# Button to trigger data scraping
scrape_button = tk.Button(root, text="Scrape Data", command=scrape_data)
scrape_button.pack(pady=10)

# Treeview for displaying scraped data
columns = ["#", "Date Posted", "Description", "Price", "Location"]
tree = ttk.Treeview(root, columns=columns, show="headings", height=10)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

tree.pack(pady=10)

# Run the GUI
root.mainloop()
