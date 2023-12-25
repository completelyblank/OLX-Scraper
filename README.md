# Olx Webscraper

This web scraper is designed to extract information about cats being sold on a famous Pakistani website similar to eBay. The scraper collects details such as the title of the selling item, its price, location, time, and description, and converts this information into a CSV file for further analysis or use.

## Prerequisites:

Python 
Beautiful Soup 
Requests 
Pandas 

## Installation:

To install the required Python libraries, run:


pip install beautifulsoup4 requests pandas
Usage
Clone this repository or download the scraper files.

Navigate to the project directory.

Run the .py script using Python:

Copy code
python scraper.py
The script will scrape the website for cat-related listings, extract the necessary information, and save it to a CSV file named cats_listings.csv in the project directory.

## Output:

The generated CSV file contains the following columns:

### Title: The title of the selling item (cat-related).
### Price: The listed price of the item.
### Location: The seller's location.
### Time: The time when the listing was posted.
### Description: Additional description about the item.

## License:
This project is licensed under the MIT License.

Acknowledgments:

This scraper is for educational purposes only.
The project was inspired by the need to collect data about cat listings on a popular Pakistani auction website.
