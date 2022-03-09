# This is InClassWeek4 Python - COMP2454
# Azarm Piran | A01195657
# Reading From CSV Files | Web Scraping | Object-Oriented Structures




# Example 1:
import pandas as pd
DRIVER_PATH = "C:\\Users\\Azarm\\PycharmProjects\\"
CSV_FILE = 'grades.csv'
dataset = { "NumericGrade":[99,98,84], "LetterGrade":['A+', 'A', 'B']}
dfOut = pd.DataFrame( data = dataset)

# Here I have decided to use a tab separator.
# The default separator is a comma which also could work.
dfOut.to_csv(DRIVER_PATH + CSV_FILE, sep='\t', index = False)

# Since I saved the file with a tab separator the instruction
# that reads the content must also use a tab separator.
dfIn = pd.read_csv(DRIVER_PATH + CSV_FILE, sep='\t')
print(dfIn.head(2))








# Exercise 1:
# Change the delimiter in Example 1 to ‘*’
import pandas as pd
DRIVER_PATH = "C:\\Users\\Azarm\\PycharmProjects\\"
CSV_FILE = 'grades.csv'
dataset = { "NumericGrade":[99,98,84], "LetterGrade":['A+', 'A', 'B']}
dfOut = pd.DataFrame( data = dataset)

dfOut.to_csv(DRIVER_PATH + CSV_FILE, sep='*')

dfIn = pd.read_csv(DRIVER_PATH + CSV_FILE, sep='*')
print(dfIn.head(2))



# Exercise 2
import pandas as pd
DRIVER_PATH = "C:\\Users\\Azarm\\PycharmProjects\\"
CSV_FILE = 'grades.csv'
dataset = { "NumericGrade":[99,98,84], "LetterGrade":['A+', 'A', 'B']}
dfOut = pd.DataFrame( data = dataset)

dfOut.to_csv(DRIVER_PATH + CSV_FILE, sep=',')

dfIn = pd.read_csv(DRIVER_PATH + CSV_FILE, sep=',')
print(dfIn.head(2))



# Selenium
# Install selenium | webdriver-manager


# Installing WebDriver
# Example 2
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
DRIVER_PATH = "C:/Users/Azarm/PycharmProjects/chromedriver"
browser = None

# This loads webdriver from the local machine if it exists.
try:
    browser = webdriver.Chrome(DRIVER_PATH)
    print("The path to webdriver_manager was found.")

# If a webdriver not found error occurs it is then downloaded.
except:
    print("webdriver not found. Update 'DRIVER_PATH' with file path in the download.")
    browser = webdriver.Chrome(ChromeDriverManager().install())




# Using Selector Gadget
# Example 3
# I have not done this example yet









# Example 4
import time
from selenium import webdriver
from bs4 import BeautifulSoup

DRIVER_PATH = "C:/Users/Azarm/PycharmProjects/chromedriver"
URL = "https://www.rottentomatoes.com/critics/latest_reviews"

browser = webdriver.Chrome(DRIVER_PATH)
browser.get(URL)

# Give the browser time to load all content.
time.sleep(3)

content = browser.find_elements_by_css_selector(".critics-latest-reviews__data-review .a")
for e in content:
    start = e.get_attribute('innerHTML')
    # Beautiful soup allows us to remove HTML tags from our content if it exists.
    soup = BeautifulSoup(start, features='lxml')
    print(soup.get_text())
    print("***")  # Go to new line.







# Exercise 4
import time
from selenium import webdriver
from bs4 import BeautifulSoup

DRIVER_PATH = "C:/Users/Azarm/PycharmProjects/chromedriver"
URL = "https://www.rottentomatoes.com/critics/latest_reviews"

browser = webdriver.Chrome(DRIVER_PATH)
browser.get(URL)

# Give the browser time to load all content.
time.sleep(3)


content = browser.find_elements_by_css_selector(".critics-latest-reviews__score")
for e in content:
    start = e.get_attribute('innerHTML')
    # Beautiful soup allows us to remove HTML tags from our content if it exists.
    soup = BeautifulSoup(start, features='lxml')
    print(soup.get_text())
    print("***")  # Go to new line.







# Exercise 5
import time
from selenium import webdriver
from bs4 import BeautifulSoup

DRIVER_PATH = "C:/Users/Azarm/PycharmProjects/chromedriver"
URL = "https://www.bcit.ca/study/programs/5512cert#courses"

browser = webdriver.Chrome(DRIVER_PATH)
browser.get(URL)

time.sleep(3)

content = browser.find_elements_by_css_selector(".clicktoshow")
for e in content:
    start = e.get_attribute('innerHTML')
    # Beautiful soup allows us to remove HTML tags from our content if it exists.
    soup = BeautifulSoup(start, features='lxml')
    print(soup.get_text())
    print("***")  # Go to new line.







# Example 5
import time
from selenium import webdriver
from bs4 import BeautifulSoup

DRIVER_PATH = "C:/Users/Azarm/PycharmProjects/chromedriver"
URL = "https://vpl.bibliocommons.com/events/search/index"

browser = webdriver.Chrome(DRIVER_PATH)
browser.get(URL)

time.sleep(3)

content = browser.find_elements_by_css_selector(".event-row")
for e in content:
    start = e.get_attribute('innerHTML')
    # Beautiful soup allows us to remove HTML tags from our content if it exists.
    soup = BeautifulSoup(start, features='lxml')
    print(soup.get_text())
    print("***")  # Go to new line.






# Example 6
# Custom Parsing
import re
import time
from selenium import webdriver
from bs4 import BeautifulSoup

DRIVER_PATH = "C:/Users/Azarm/PycharmProjects/chromedriver"
URL = "https://vpl.bibliocommons.com/events/search/index"

browser = webdriver.Chrome(DRIVER_PATH)
browser.get(URL)

time.sleep(3)

content = browser.find_elements_by_css_selector(".event-row")
for e in content:
    textContent = e.get_attribute('innerHTML')
    # Beautiful soup removes HTML tags from our content if it exists.
    soup = BeautifulSoup(textContent, features="lxml")
    rawString = soup.get_text().strip()

    # Remove hidden characters for tabs and new lines.
    rawString = re.sub(r"[\n\t]*", "", rawString)

    # Replace two or more consecutive empty spaces with '*'
    rawString = re.sub('[ ]{2,}', '*', rawString)
    # Fine tune the results so they can be parsed.
    rawString = rawString.replace("Location", "Location*")
    rawString = rawString.replace("Registration closed", "Registration closed*")
    rawString = rawString.replace("Registration required", "Registration required*")
    rawString = rawString.replace("In Progress", "*In Progress*")
    rawString = rawString.replace("*/*", "/")
    rawString = rawString.replace("Full*", "*Full*")

    print(rawString)
    print("***")








# Example 7
# Cleaning Up Our Output
import re
import time
from selenium import webdriver
from bs4 import BeautifulSoup

DRIVER_PATH = "C:/Users/Azarm/PycharmProjects/chromedriver"
URL = "https://vpl.bibliocommons.com/events/search/index"

browser = webdriver.Chrome(DRIVER_PATH)
browser.get(URL)

time.sleep(3)

content = browser.find_elements_by_css_selector(".event-row")
for e in content:
    textContent = e.get_attribute('innerHTML')
    # Beautiful soup removes HTML tags from our content if it exists.
    soup = BeautifulSoup(textContent, features="lxml")
    rawString = soup.get_text().strip()

    # Remove hidden characters for tabs and new lines.
    rawString = re.sub(r"[\n\t]*", "", rawString)

    # Replace two or more consecutive empty spaces with '*'
    rawString = re.sub('[ ]{2,}', '*', rawString)
    # Fine tune the results so they can be parsed.
    rawString = rawString.replace("Location", "Location*")
    rawString = rawString.replace("Registration closed", "Registration closed*")
    rawString = rawString.replace("Registration required", "Registration required*")
    rawString = rawString.replace("In Progress", "*In Progress*")
    rawString = rawString.replace("*/*", "/")
    rawString = rawString.replace("Full*", "*Full*")

    #print(rawString)
    #print("***")
    eventArray = rawString.split('*')

    EVENT_NAME = 0
    EVENT_DATE = 1
    EVENT_TIME = 2
    eventName = eventArray[EVENT_NAME]
    eventDate = eventArray[EVENT_DATE].strip()  # remove leading and trailing spaces
    eventTime = eventArray[EVENT_TIME].strip()  # remove leading and trailing spaces
    location = eventArray[len(eventArray) - 1]
    print("Name:     " + eventName)
    print("Date:     " + eventDate)
    print("Time:     " + eventTime)
    print("Location: " + location)
    print("***")




# Example 8
# Clicking








# Example 9:
# Sending Keys

import time
import re
from selenium import webdriver
from bs4 import BeautifulSoup

# driver = webdriver.Chrome(ChromeDriverManager().install())
DRIVER_PATH = "C:/Users/Azarm/PycharmProjects/chromedriver"
URL = "https://animalfactguide.com/links/"

browser = webdriver.Chrome(DRIVER_PATH)
browser.get(URL)

time.sleep(3)

# Find the search input.
search = browser.find_element_by_css_selector("#s")
# Writing the word "Zebra" in the search box
search.send_keys("Zebra")

# Find the search button - this is only enabled when a search query is entered
button = browser.find_element_by_css_selector("#searchsubmit")
button.click()  # Click the button.

# Extracts text from scraped content.
def extractText(data):
    text = data.get_attribute('innerHTML')
    soup = BeautifulSoup(text, features="lxml")
    content = soup.get_text()
    return content

titles = browser.find_elements_by_css_selector(".entry-title a")
descriptions = browser.find_elements_by_css_selector(".entry-summary p")

titleList = []
descriptionList = []

for i in range(0, len(titles)):
    # extract title and add to list.
    title = extractText(titles[i])
    titleList.append(title)

    # extract description and add to list.
    description = extractText(descriptions[i])
    descriptionList.append(description)

# Show the content.
for i in range(0, len(descriptionList)):
    print("\n********************")
    print("Title:       " + titleList[i])
    print("Description: " + descriptionList[i])




# Example 10:
# Object-Oriented Structures
# Class Declaration
class Child:  # Declare class.
    age = 5  # Declare and initialize property.


girl = Child()  # Create object.
print(girl.age)  # Show property of object.






# Example 11:
# Class with Constructor and Method
class Child:
    age = 0
    firstName = ""

    # This is our constructor. It initializes variables when the object is created.
    def __init__(self, firstName, age):
        self.firstName = firstName
        self.age = age

    # Declare a function to display details about the child.
    def showDetail(self):
        print("The child's name is:   " + self.firstName);
        print(self.firstName + "'s age is: " + str(self.age));


childA = Child("Jenny", 5)
childA.showDetail()








# Exercise 13:
class bankAccount:
    accountNumber = 0
    balance = 0
    firstName = ""
    lastName = ""

    def __init__(self, accountNumber, balance, firstName,lastName):
        self.accountNumber = accountNumber
        self.balance = balance
        self.firstName = firstName
        self.lastName = lastName

    def showInterest(self):
        print("Your balance after 3% interest is:   " + str((self.balance * 0.3) + self.balance));


    def showFullName(self):
        print("Account owner's name is:   " + self.firstName + " " + self.lastName);
        print("Account number is:   " + str(self.accountNumber));
        print("Account balance is:   " + str(self.balance));

customer1 = bankAccount(123456,100,"Azarm","Piran")
customer1.showInterest()
customer1.showFullName()








# Example 12
class Child:  # Declare class.
    age = 0  # Declare and initialize age property.
    firstName = ""  # Declare and initialize firstName property.

    # This is our constructor. It initializes variables when the object is created.
    def __init__(self, firstName, age):
        self.firstName = firstName
        self.age = age

    # Declare a function to display details about the child.
    def showDetail(self):
        print("The child's name is:   " + self.firstName);
        print(self.firstName + "'s age is: " + str(self.age));


# Create a list of children.
childA = Child("Jenny", 5)
childB = Child("Tom", 6)
childC = Child("Amir", 5)
childD = Child("Harp", 5)
childList = [childA, childB, childC, childD]

# We can easily display object detail without concern for the internal data & logic.
for child in childList:
    child.showDetail()
    print("\n")






# 146 min
# Exercise 14
import re
import time
from selenium import webdriver
from bs4 import BeautifulSoup

DRIVER_PATH = "C:/Users/Azarm/PycharmProjects/chromedriver"
URL = "https://vpl.bibliocommons.com/events/search/index"

browser = webdriver.Chrome(DRIVER_PATH)
browser.get(URL)

time.sleep(3)

content = browser.find_elements_by_css_selector(".event-row")


class LibraryEvent:
    eventName = ""
    eventDate = ""
    eventTime = ""
    eventLocation = ""

    def __init__(self, eventName, eventDate,eventTime,eventLocation):
        self.eventName = eventName
        self.eventDate = eventDate
        self.eventTime = eventTime
        self.eventLocation = eventLocation

    def showDetail(self):
        print("Name:     " + eventName)
        print("Date:     " + eventDate)
        print("Time:     " + eventTime)
        print("Location: " + eventLocation)
        print("***")


eventList = []

for e in content:
    textContent = e.get_attribute('innerHTML')
    soup = BeautifulSoup(textContent, features="lxml")
    rawString = soup.get_text().strip()
    rawString = re.sub(r"[\n\t]*", "", rawString)
    rawString = re.sub('[ ]{2,}', '*', rawString)
    rawString = rawString.replace("Location", "Location*")
    rawString = rawString.replace("Registration closed", "Registration closed*")
    rawString = rawString.replace("Registration required", "Registration required*")
    rawString = rawString.replace("In Progress", "*In Progress*")
    rawString = rawString.replace("*/*", "/")
    rawString = rawString.replace("Full*", "*Full*")

    eventArray = rawString.split('*')

    EVENT_NAME = 0
    EVENT_DATE = 1
    EVENT_TIME = 2
    EVENT_LOCATION = 3

    eventName = eventArray[EVENT_NAME]
    eventDate = eventArray[EVENT_DATE].strip()
    eventTime = eventArray[EVENT_TIME].strip()
    eventLocation = eventArray[len(eventArray) - 1]
    eventObject = LibraryEvent(eventName,eventDate, eventTime,eventLocation)

    eventList.append(eventObject)


for e in eventList:
    eventObject.showDetail()
    print("\n")



























