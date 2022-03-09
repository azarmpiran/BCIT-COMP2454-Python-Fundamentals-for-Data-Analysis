# Homework 2
# Azarm Piran | A01195657

import time
import re
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

DRIVER_PATH = "C:/Users/Azarm/PycharmProjects/chromedriver"
URL = "https://www.walmart.ca/en"

browser = webdriver.Chrome(DRIVER_PATH)
browser.get(URL)

time.sleep(3)

SEARCH_TERM = "Cheese"

search = browser.find_element_by_css_selector(".eesbt950")
search.send_keys(SEARCH_TERM)

button = browser.find_element_by_css_selector(".e1xoeh2i2")
button.click()



class Cheese:
    brand = ""
    weight = 0
    price = 0



    def __init__(self, brand, weight,price):
        self.brand = brand
        self.weight = weight
        self.price = price

    def showDetail(self):
        print("brand:     " + brand)
        print("weight:    " + weight)
        print("price:     " + price)



cheeseList = []
productList = []

pageNum = 1;
for i in range(0, 3):
    content = browser.find_elements_by_css_selector(".css-2vqe5n , .eudvd6x0")

    for e in content:
        textContent = e.get_attribute('innerHTML')
        soup = BeautifulSoup(textContent, features="lxml")
        rawString = soup.get_text().strip()
        rawString = re.sub(r"[\n\t]*", "", rawString)
        rawString = re.sub('[ ]{2,}', '*', rawString)
        cheeseList.append(rawString)


    pageNum += 1
    print("*************************************************************************")
    print("pageNum: " + str(pageNum))

    URL_NEXT = "https://www.walmart.ca/search?q=" + SEARCH_TERM + "&p="
    URL_NEXT = URL_NEXT + str(pageNum)
    browser.get(URL_NEXT)

    time.sleep(3)
#print(cheeseList)
print("done loop")


length = int((len(cheeseList)/3)-1)
x = 0
y = 1
z = 2
for i in range(length):
    brand = cheeseList[x]
    weight = cheeseList[y]
    price = cheeseList[z]
    cheeseObject = Cheese(brand, weight, price)
    productList.append(cheeseObject)
    cheeseObject.showDetail()
    print("\n")
    x = x + 3
    y = y + 3
    z = z + 3



productDf = pd.DataFrame()

for product in productList:
    productDf = productDf.append({'Brand': product.brand,'Weight': product.weight,'Price': product.price}, ignore_index=True)

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print(productDf)
print('\n')



# Part 1 - g
DRIVER_PATH = "C:\\Users\\Azarm\\PycharmProjects\\"
CSV_FILE = 'walmart.csv'
productDfOut = pd.DataFrame(data=productDf)
productDfOut.to_csv(DRIVER_PATH + CSV_FILE, sep=',')
productDfIn = pd.read_csv(DRIVER_PATH + CSV_FILE, sep=',')

# Removing Unnamed column
productDfIn = productDfIn.loc[:, ~productDfIn.columns.str.contains('^Unnamed')]

# First and last 2 rows of data
print('\n')
print('First 2 rows of Data Frame:')
print(productDfIn.head(2))
print('\n')
print('Last 2 rows of Data Frame:')
print(productDfIn.tail(2))

