# Homework 2 | Part B
# Azarm Piran | A01195657

import time
import re
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine




DRIVER_PATH = "C:/Users/Azarm/PycharmProjects/chromedriver"
URL = "https://news.google.com/covid19/map?hl=en-CA&gl=CA&ceid=CA%3Aen&mid=%2Fm%2F0d060g"

browser = webdriver.Chrome(DRIVER_PATH)
browser.get(URL)

time.sleep(3)



covidList = []

content = browser.find_elements_by_css_selector(".YvL7re .l3HOY:nth-child(6) , .YvL7re .l3HOY:nth-child(5) , .YvL7re .l3HOY:nth-child(3) , .YvL7re th+ .l3HOY , .YvL7re .pcAJd")
for e in content:
    textContent = e.get_attribute('innerHTML')
    soup = BeautifulSoup(textContent, features="lxml")
    rawString = soup.get_text().strip()
    rawString = re.sub(r"[\n\t]*", "", rawString)
    rawString = re.sub('[ ]{2,}', '*', rawString)
    covidList.append(rawString)



class Covid:
    province = ''
    totalCases = 0
    newCases = 0
    casesPerOneMillion = 0
    death = 0

    def __init__(self, province, totalCases, newCases, casesPerOneMillion, death):
        self.province = province
        self.totalCases = totalCases
        self.newCases = newCases
        self.casesPerOneMillion = casesPerOneMillion
        self.death = death


covidDataList = []

length = int((len(covidList)/5)-1)
a = 0
b = 1
c = 2
d = 3
e = 4

for i in range(length):
    province = covidList[a]
    totalCases = covidList[b]
    newCases = covidList[c]
    casesPerOneMillion = covidList[d]
    death = covidList[e]

    covidObject = Covid(province, totalCases, newCases, casesPerOneMillion, death)
    covidDataList.append(covidObject)
    print("\n")
    a = a + 5
    b = b + 5
    c = c + 5
    d = d + 5
    e = e + 5



covidDf = pd.DataFrame()

for c in covidDataList:
    covidDf = covidDf.append({'Province': c.province,'TotalCases': c.totalCases,'NewCases': c.newCases, 'CasesPer1MillionPeople': c.casesPerOneMillion, 'Death': c.death}, ignore_index=True)

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

#print(covidDf)



def showQueryResult(sql):
    engine = create_engine('sqlite://', echo=False)
    connection = engine.connect()
    covidDf.to_sql(name='covidTable', con=connection, if_exists='replace', index=False)
    queryResult = pd.read_sql(sql, connection)
    return queryResult


print("*****************************************************************************")
print("Covid Data per each Canadian Province:")
SQL = "SELECT Province,TotalCases AS [Total Cases], NewCases AS [New Cases], Death  FROM covidTable "
results = showQueryResult(SQL)
print(results)
print("*****************************************************************************")


print("Summary of Covid cases in CANADA:")
SQL = "SELECT SUM(Death) AS [Total Death Cases], SUM(TotalCases) AS [Total Cases] FROM covidTable "
totalResults = showQueryResult(SQL)
print(totalResults)
print("*****************************************************************************")



plt.bar(results['Province'], results['Death'], color='green')
plt.xticks(rotation='vertical')
plt.title("Covid Death Cases per Province")
plt.show()

