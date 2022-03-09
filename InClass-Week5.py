# Example 1

import pandas as pd
from   sqlalchemy import create_engine

PATH     = "C:\\Users\\Azarm\\Desktop\\BCIT\\Python\\DataSet\\"
CSV_DATA = "brazil_forestFires.csv"

df = pd.read_csv(PATH + CSV_DATA, skiprows=1,  encoding = "ISO-8859-1", sep=',',
                 names=('year', 'state',  'month', 'number','date', ))
print(df.tail(2))

DB_FILE    = 'forestFire.db'
engine     = create_engine('sqlite:///' + PATH + DB_FILE, echo=False)
connection = engine.connect()

df.to_sql(name='brazilForest', con=connection, if_exists='replace', index=False)



---------------------------------------------------------------------------------

# Example 2

import pandas as pd
from   sqlalchemy import create_engine

PATH     = "C:\\Users\\Azarm\\Desktop\\BCIT\\Python\\DataSet\\"
CSV_DATA = "brazil_forestFires.csv"

df = pd.read_csv(PATH + CSV_DATA, skiprows=1,  encoding = "ISO-8859-1", sep=',',
                 names=('year', 'state',  'month', 'number','date', ))
print(df.tail(2))

DB_FILE    = 'forestFire.db'
engine     = create_engine('sqlite:///' + PATH + DB_FILE, echo=False)
connection = engine.connect()

df.to_sql(name='brazilForest', con=connection, if_exists='replace', index=False)


# Placed query in this function to enable code re-usuability.
def showQueryResult(sql, dbconnection):
    print("\n*** Showing SQL statement")
    print(sql)
    # Perform query
    subDf = pd.read_sql(sql, dbconnection)
    print("\n*** Showing dataframe summary")
    return subDf


# Get DataFrame contents for 'Rio' and 'Sao Paulo' only.
sql = "SELECT * FROM " + "brazilForest" \
      + " WHERE state = 'Rio' OR state='Sao Paulo' " \
      + " ORDER BY date"

newDf = showQueryResult(sql, connection)
print(newDf.tail())




---------------------------------------------------------------------------------

# Exercise 3
import pandas as pd
from sqlalchemy import create_engine

PATH = "C:\\Users\\Azarm\\Desktop\\BCIT\\Python\\DataSet\\"

DB_FILE = 'ramenReviews.db'
engine = create_engine('sqlite:///' + PATH + DB_FILE, echo=False)
connection = engine.connect()

def showQueryResult(sql, dbconnection):
    print("\n*** Showing SQL statement")
    print(sql)
    # Perform query
    subDf = pd.read_sql(sql, dbconnection)
    print("\n*** Showing dataframe summary")
    return subDf

sql = "SELECT * FROM " + "Review"

newDf = showQueryResult(sql, connection)
print(newDf.tail())




---------------------------------------------------------------------------------

# Example 3

import openpyxl
import pandas as pd

PATH = "C:\\Users\\Azarm\\Desktop\\BCIT\\Python\\DataSet\\"
FILE_NAME = "Tides.xlsx"
df = pd.read_excel(PATH + FILE_NAME, sheet_name='Sheet1')
df.to_excel(PATH + "NewFile.xlsx", sheet_name='Sheet1')
print (df)


---------------------------------------------------------------------------------

# Example 5
# Showing DataFrames as HTML
import pandas as pd
from IPython.display import Image
from IPython.display import display_html
from IPython.core.display import display, HTML
import matplotlib.pyplot as plt

# Create and show budget dataframe.
df = pd.DataFrame(columns=["Week", "Cost", "Revenue"])
df['Week']    = ['1','2','3','4']
df['Cost']    = [8,10,12,14]
df['Revenue'] = [6,12,14,16]
print(df)

    
#display_side_by_side(df,df)
# Here, we have our data as a dataframe! we saved it in a df. --- now we turn df to a html using to.html() function
html_str = df.to_html()
#print(html_str)
display_html(html_str.replace('table','table style="display:inline;"'),raw=True)





---------------------------------------------------------------------------------


# Example 6: 
# Showing DataFrames Side by Side
# in the previous example we saw how to print 2 different formats for df, if you want to print them next to each other you can use this function

import pandas as pd
from IPython.display import Image
from IPython.display import display_html
from IPython.core.display import display, HTML
import matplotlib.pyplot as plt

# Create and show budget dataframe.
df = pd.DataFrame(columns=["Week", "Cost", "Revenue"])
df['Week']    = ['1','2','3','4']
df['Cost']    = [8,10,12,14]
df['Revenue'] = [6,12,14,16]

def display_side_by_side(*args):
    html_str=''
    for item in args:
        html_str+=item.to_html()
    display_html(html_str.replace('table','table style="display:inline;"'),raw=True)

display_side_by_side(df,df)



---------------------------------------------------------------------------------

# Example 7: 
# Showing Multiple Graphs on One Line

import pandas as pd
from IPython.display import Image
from IPython.display import display_html
from IPython.core.display import display, HTML
import matplotlib.pyplot as plt

# Create and show budget dataframe.
df = pd.DataFrame(columns=["Week", "Cost", "Revenue"])
df['Week']    = ['1','2','3','4']
df['Cost']    = [8,10,12,14]
df['Revenue'] = [6,12,14,16]


# First chart.
plt.figure(figsize=(6,1.3))
plt.subplot(1, 2, 1) # 1 row. Two columns. 1st cell.
plt.plot(df['Week'], df['Cost'], color='red')
plt.ylim((6,16))

# Second chart.
plt.subplot(1, 2, 2) # 1 row. Two columns. 2nd cell.
plt.plot(df['Week'], df['Revenue'], color='green')
plt.ylim((6,16))

# Show plots.
plt.show() 



---------------------------------------------------------------------------------


# Example 8: 
# Embedding HTML

display(HTML("<h1>This is html code.</h1>"))

# We can use display() to show HTML from Python. 
# HTML() converts encoded content the raw content.
display(HTML("<h4>This text and image are rendered using html embedded in Python code.</h4>"))

# This image is stored at the Jupyter notebook root folder.
img=Image(url= "files/Photo.png")
display(img)  
 



---------------------------------------------------------------------------------





---------------------------------------------------------------------------------






---------------------------------------------------------------------------------






---------------------------------------------------------------------------------





---------------------------------------------------------------------------------






---------------------------------------------------------------------------------



---------------------------------------------------------------------------------






---------------------------------------------------------------------------------





---------------------------------------------------------------------------------






---------------------------------------------------------------------------------






---------------------------------------------------------------------------------





---------------------------------------------------------------------------------






---------------------------------------------------------------------------------






---------------------------------------------------------------------------------





---------------------------------------------------------------------------------








---------------------------------------------------------------------------------



---------------------------------------------------------------------------------






---------------------------------------------------------------------------------





---------------------------------------------------------------------------------






---------------------------------------------------------------------------------






---------------------------------------------------------------------------------





---------------------------------------------------------------------------------






---------------------------------------------------------------------------------






---------------------------------------------------------------------------------





---------------------------------------------------------------------------------







---------------------------------------------------------------------------------



---------------------------------------------------------------------------------






---------------------------------------------------------------------------------





---------------------------------------------------------------------------------






---------------------------------------------------------------------------------






---------------------------------------------------------------------------------





---------------------------------------------------------------------------------






---------------------------------------------------------------------------------






---------------------------------------------------------------------------------





---------------------------------------------------------------------------------