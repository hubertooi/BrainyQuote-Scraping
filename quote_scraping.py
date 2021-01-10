# import packages requests, bs4, and pandas
import requests
from bs4 import BeautifulSoup
import pandas as pd

# topic input and pages input
topic = input("Enter the type of quotes: ")
pages = input("Enter the pages: ")

quote_list = []  # quote_List to store data

# for loop to iterate through pages number with range
for page in range(1, int(pages) + 1, 1):
    # url from BrainyQuote
    url = f'https://www.brainyquote.com/topics/{topic}-quotes_{page}'
    r = requests.get(url)  # requests.get the url as r
    print(url)  # print out the url for user to check if it is available
    bs = BeautifulSoup(r.content, 'html.parser')

    # find all quotes in the web page with div tag with its associated class attribute
    quotes = bs.find_all("div", {'class': 'm-brick grid-item boxy bqQt r-width'})

    # for loop to iterate through quotes
    for each in quotes:
        # Each quote can be obtain either through a tag with class attribute within its img tag with alt attribute
        # a tag with title attribute will retrieve both quote and author if the previous did not capture data
        quote = each.find('a', {'class': 'oncl_q'}).find('img').get('alt') if (each.find('a', {'class': 'oncl_q'}).find('img') is not None) else f"{each.find('a', {'title': 'view quote'}).text.strip()} - {each.find('a', {'title': 'view author'}).text.strip()} "

        # quote_items group data in json format
        quote_items = {
            'quote': quote
        }
        # quote_items are appended to quote_List
        quote_list.append(quote_items)

# Using pandas DataFrame to create tabular for quote_List
df = pd.DataFrame(quote_list)

# This is the path where you will have to determine before you run
path = 'C:\\Users\\Hubert\\Desktop\\'+f'quotes_{topic}.csv'

# Print out the path where you save the csv file, it is like a reminder for you
print("The path where csv file is save: " + path)

# df.to_csv converts tabular data to csv format with index set to False to not include pandas indexing
df.to_csv(path, index=False)
