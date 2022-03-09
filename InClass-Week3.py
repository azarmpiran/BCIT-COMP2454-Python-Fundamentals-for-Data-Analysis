# InClass3
# Azarm Piran
# A01195657

unformattedInt = '233'
wholeNumber = int(unformattedInt)
print(wholeNumber)
unformattedFloat = '12.99'
print(unformattedFloat)
floatNumber = float(unformattedFloat)
print(wholeNumber + floatNumber)


# Try - Except
wholeNumber   = int("abc")
print(wholeNumber)



# Exmaple 2
def convertStringToFloat(alphaStr):
    try:
        floatNumber = float(alphaStr)
        formattedFloat = round(floatNumber, 2)
        print("The value has successfully been converted.")
        print(formattedFloat)
        return formattedFloat
    except Exception as e:
        error = str(e)
        print(error)
        return None  # None represents a null object in Python.

formattedValue = convertStringToFloat("azarm")
if (formattedValue != None):
    print("The converted value is: ", str(formattedValue))
else :
    print('could not be converted to a float.')



# Exercise 1
# This function performs division. It does not print anything.
def convertStringToFloat(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except Exception as e:
        return None
# your code goes here.

def showResult(result):
    if (result != None):
        print("The value is " + str(result))
    else:
        print("An error occurred during the division.")


result = convertStringToFloat(15, 5)
showResult(result)

print("")
result = convertStringToFloat(15, 0)
showResult(result)

print("")
result = convertStringToFloat(21, 3)
showResult(result)

print("")
result = convertStringToFloat(0, 3)
showResult(result)




# Exercise 2
def convertStringToFloat(numerator, denominator):
    firstName = 'Azarm'
    print(firstName)
    def lastNameFunction(lastName):
        lastName = lastName
        print(lastName)
        breakpoint()
    try:
        result = numerator / denominator
        return result
    except Exception as e:
        return None
# your code goes here.

def showResult(result):
    if (result != None):
        print("The value is " + str(result))
    else:
        print("An error occurred during the division.")


result = convertStringToFloat(15, 5)
showResult(result)

print("")
result = convertStringToFloat(15, 0)
showResult(result)

print("")
result = convertStringToFloat(21, 3)
showResult(result)

print("")
result = convertStringToFloat(0, 3)
showResult(result)




























# Example 3
# Local scope
def displayContent(x):
    #a = 25 # The number is born here.
    print('Inside the function the variable \'a\'=' + str(a))
    print('The parameter x=' + str(x))
    return # Locally declared variables die here when the function exits.

a = 100
displayContent(a)
print("The global value for \'a\'=" + str(a))


# Exercise 3
















# Example 4:
# Line Graphs
import numpy as np
import matplotlib.pyplot as plt

years = [2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
colorado = [5029196,5029316,5048281,5121771,5193721,5270482,5351218,5452107,
               5540921,5615902,5695564]
connecticut = [3574097,3574147,3579125,3588023,3594395,3594915,3594783,3587509,
               3578674,3573880,3572665]
# red dashes, blue squares and green triangles
plt.plot(years, colorado, "--", color='red', label="Colorado")
#plt.show()
plt.plot(years,connecticut, "s", color='blue', label="Connecticut")
#plt.show()

# legend
# https://matplotlib.org/users/legend_guide.html
plt.ylim(ymin=0)  # Set's y axis start to 0.
#plt.show()
plt.legend(loc=0)
#plt.show()
plt.xlabel("Year")
plt.ylabel("Population")
plt.title('Population by State')

plt.show()




# Exercise 4
import numpy as np
import matplotlib.pyplot as plt

years = [2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
colorado = [5029196,5029316,5048281,5121771,5193721,5270482,5351218,5452107,
               5540921,5615902,5695564]
connecticut = [3574097,3574147,3579125,3588023,3594395,3594915,3594783,3587509,
               3578674,3573880,3572665]
delaware = [897934,897934,899595,907316,915188,923638,932596,941413,949216,
               957078,967171]


# red dashes, blue squares and green triangles
plt.plot(years, colorado, "--", color='red', label="Colorado")
plt.plot(years,connecticut, "s", color='black', label="Connecticut")
plt.plot(years,delaware, "", color='green', label="delaware")

# legend
# https://matplotlib.org/users/legend_guide.html
plt.ylim(ymin=0)  # Set's y axis start to 0.
#plt.show()
#plt.legend(loc='upper left')
#plt.legend(handles=[p1, p2], title='title', bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)
#plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
plt.legend(loc='center left', bbox_to_anchor=(0.70, 0.74) , shadow=True)
#plt.show()
plt.xlabel("Year")
plt.ylabel("Population")
plt.title('Population by State')

plt.show()



# Example 5:
# Simple Scatter Plot
import matplotlib.pyplot as plt
# Plot scatter of x and y coordinates.
time_X = [0.1, 0.2, 0.3, 0.4, 0.5, 0.2]
growth_Y = [0.1, 0.15, 0.4,  0.6, 0.44, 0.17]
plt.scatter(time_X, growth_Y, color='green', label='Bacteria A')

# Add a legend, axis labels, and title.
plt.legend()
plt.xlabel("Time (Hours)")
plt.ylabel("Growth")
plt.title('Bacteria Growth Over Time')

plt.show()



# Exercise 5
import matplotlib.pyplot as plt
pounds  = [120, 110, 160]
inches  = [50, 48, 68]
plt.scatter(pounds, inches, color='orange', label='Students Region A')
plt.legend()
plt.xlabel("Weight (Pounds)")
plt.ylabel("Height (Inches)")
plt.title('Height vs Weight for students Region A')

plt.show()


# Exercise 6
import matplotlib.pyplot as plt
poundsA  = [120, 110, 160]
inchesA  = [50, 48, 68]
poundsB  = [121, 108, 150, 121, 121, 146]
inchesB  = [49, 45, 85, 46, 50, 85]

plt.scatter(poundsA, inchesA, color='orange', label='Students Region A')
plt.scatter(poundsB, inchesB, color='green', label='Students Region B')
plt.legend()
plt.xlabel("Weight (Pounds)")
plt.ylabel("Height (Inches)")
plt.title('Height vs Weight for students Region A and B')
plt.show()



# Example 6:
# Bar Plots
import matplotlib.pyplot as plt
x = ['Nuclear', 'Hydro', 'Gas', 'Oil', 'Coal', 'Biofuel']
energy = [5, 6, 15, 22, 24, 8]

plt.bar(x, energy, color='green')
plt.xlabel("Energy Source")
plt.ylabel("Energy Output (GJ)")
plt.title("Energy output from various fuel sources")

plt.xticks(x, x)
plt.show()



# Exercise 7
# Example 7:
# Grouped Bar Plots
import matplotlib.pyplot as plt
import numpy as np
NUM_MEANS = 5
NUM_GROUPS = 3
bc_means = [20, 35, 30, 35, 27]
alberta_means = [25, 32, 34, 20, 25]
saskatchewan_means = [18, 28, 32, 24, 31]
ind = np.arange(NUM_MEANS)
print(ind)
width = 0.2
plt.bar(ind, bc_means, width, label='BC')
plt.bar(ind + width, alberta_means, width, label='AB')
plt.bar(ind + width + width, saskatchewan_means, width, label='SK')

plt.ylabel('Revenue')
plt.title('Quarterly Revenue by Province')

plt.xticks(ind + width / NUM_GROUPS, ('Q1', 'Q2', 'Q3', 'Q4', 'Q5'))
plt.legend(loc='best')
plt.show()





# Example 8:
# Histogram Introduction
import pandas as pd
import matplotlib.pyplot as plt

path = "C:/babysamp-98.txt"
df = pd.read_csv(path, skiprows=1,
                   sep='\t',
                   names=('MomAge', 'DadAge', 'MomEduc', 'MomMarital', 'numlive',
                          "dobmm", 'gestation', 'sex', 'weight', 'prenatalstart',
                          'orig.id', 'preemie'))
# Show all columns.
pd.set_option('display.max_columns', None)

# Increase number of columns that display on one line.
pd.set_option('display.width', 1000)

plt.hist(df["MomAge"], bins=22)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title('Mother Age')

plt.show()



# Example 9:
# Drawing Multiple Graphs on One Line
import pandas as pd
import matplotlib.pyplot as plt

# Import data into a DataFrame.
path = "C:/babysamp-98.txt"
df = pd.read_csv(path, skiprows=1,
                 sep='\t',
                 names=('MomAge', 'DadAge', 'MomEduc', 'MomMarital', 'numlive',
                        "dobmm", 'gestation', 'sex', 'weight', 'prenatalstart',
                        'orig.id', 'preemie'))

# Show all columns.
pd.set_option('display.max_columns', None)

# Increase number of columns that display on one line.
pd.set_option('display.width', 1000)
# This line allows us to set the figure size supposedly in inches.
# When rendered in the IDE the output often does not translate to inches.
plt.subplots(nrows=2, ncols=3, figsize=(14, 7))
#plt.show()
plt.subplot(2, 3, 1)  # Specfies total rows, columns and image #
#plt.show()
# where images are drawn clockwise.
plt.hist(df["MomAge"], bins=10)
plt.show()

plt.xlabel("Mom Age")
plt.ylabel("Frequency")
# plt.title('Mother Age')
plt.show()
plt.subplot(2, 3, 2)
plt.hist(df["MomEduc"], bins=10)
plt.xlabel("Mom Education")
plt.ylabel("Frequency")

# 1 is married
# 2 is unmarried
plt.subplot(2, 3, 3)
plt.hist(df["MomMarital"], bins=10)
t11 = ['', 'Y', 'N']
plt.xticks(range(len(t11)), t11, rotation=50)

# plt.xticks(['Mar', '2'], rotation=50)
plt.xlabel("Mom Married")
plt.ylabel("Frequency")

# 1 is married. 2 is unmarried.
plt.subplot(2, 3, 4)
plt.hist(df["numlive"], bins=10)
plt.xlabel("# Kids")
plt.ylabel("Frequency")

plt.subplot(2, 3, 5)  # of rows, # of columns, # plots.
plt.hist(df["DadAge"], bins=22)
plt.xlabel("Dad Age")
plt.ylabel("Frequency")

plt.subplot(2, 3, 6)
plt.hist(df["dobmm"], bins=12)
plt.xlabel("Birth Month")
plt.ylabel("Frequency")

plt.show()






# Exercise 8
import pandas as pd
import matplotlib.pyplot as plt

# Import data into a DataFrame.

path = "C:/bodyfat.txt"
df = pd.read_csv(path, skiprows=1,
                   sep='\t',
                   names=('Density', 'Pct.BF', 'Age', 'Weight', 'Height',
                           'Neck', 'Chest', 'Abdomen', 'Waist', 'Hip', 'Thigh',
                          'Ankle', 'Knee', 'Bicep', 'Forearm', 'Wrist'))

plt.subplots(nrows=3, ncols=3, figsize=(50, 50))
# 1
plt.subplot(2, 2, 1)
plt.hist(df["Pct.BF"], bins=10)
plt.xlabel("Pct.BF")
#plt.show()

# 2
plt.subplot(2, 2, 2)
plt.hist(df["Age"], bins=10)
plt.xlabel("Age")
#plt.show()

# 3
plt.subplot(2, 2, 3)
plt.hist(df["Weight"], bins=10)
plt.xlabel("Weight")
#plt.show()

# 4
plt.subplot(2, 2, 4)
plt.hist(df["Height"], bins=10)
plt.xlabel("Height")
plt.show()





# Example 10: - Exercise 9
# Retail SQL
import pandas as pd
from sqlalchemy import create_engine

# The data file path and file name need to be configured.
PATH = "C:/"
CSV_DATA = "retailerDB.csv"
df = pd.read_csv(PATH + CSV_DATA)

# Placed query in this function to enable code re-usuability.
def showQueryResult(sql):
    # This code creates an in-memory table called 'RetailInventory '.
    engine = create_engine('sqlite://', echo=False)
    connection = engine.connect()
    df.to_sql(name='RetailInventory', con=connection, if_exists='replace', index=False)

    # This code performs the query.
    queryResult = pd.read_sql(sql, connection)
    return queryResult

# Read all rows from the table.
SQL = "SELECT * FROM RetailInventory "
results = showQueryResult(SQL)
print(results)



# Exercise 11:
# Filtering with a WHERE clause
import pandas as pd
from sqlalchemy import create_engine

# The data file path and file name need to be configured.
PATH = "C:/"
CSV_DATA = "retailerDB.csv"
df = pd.read_csv(PATH + CSV_DATA)

# Placed query in this function to enable code re-usuability.
def showQueryResult(sql):
    # This code creates an in-memory table called 'Inventory'.
    engine = create_engine('sqlite://', echo=False)
    connection = engine.connect()
    df.to_sql(name='Inventory', con=connection, if_exists='replace', index=False)

    # This code performs the query.
    queryResult = pd.read_sql(sql, connection)
    return queryResult

# Read all rows from the table.
SQL     = "SELECT * FROM Inventory WHERE price >= 4 "
results = showQueryResult(SQL)
print(results)




# Exercise 12
import pandas as pd
from sqlalchemy import create_engine

# The data file path and file name need to be configured.
PATH     = "C:/"
CSV_DATA = "retailerDB.csv"
df       = pd.read_csv(PATH + CSV_DATA)

# Placed query in this function to enable code re-usuability.
def showQueryResult(sql):
    # This code creates an in-memory table called 'Inventory'.
    engine     = create_engine('sqlite://', echo=False)
    connection = engine.connect()
    df.to_sql(name='Inventory', con=connection, if_exists='replace', index=False)

    # This code performs the query.
    queryResult = pd.read_sql(sql, connection)
    return queryResult

# Read all rows from the table.
SQL     = "SELECT * FROM Inventory ORDER BY productName"
results = showQueryResult(SQL)
print(results)




# Exercise 13
import pandas as pd
from sqlalchemy import create_engine

# The data file path and file name need to be configured.
PATH     = "C:/"
CSV_DATA = "retailerDB.csv"
df       = pd.read_csv(PATH + CSV_DATA)

# Placed query in this function to enable code re-usuability.
def showQueryResult(sql):
    # This code creates an in-memory table called 'Inventory'.
    engine     = create_engine('sqlite://', echo=False)
    connection = engine.connect()
    df.to_sql(name='Inventory', con=connection, if_exists='replace', index=False)

    # This code performs the query.
    queryResult = pd.read_sql(sql, connection)
    return queryResult

# Read all rows from the table.
SQL     = "SELECT productName,vendor,quantity,price FROM Inventory ORDER BY productName,quantity"
results = showQueryResult(SQL)
print(results)






# Exercise 14
import pandas as pd
from sqlalchemy import create_engine

# The data file path and file name need to be configured.
PATH     = "C:/"
CSV_DATA = "retailerDB.csv"
df       = pd.read_csv(PATH + CSV_DATA)

# Placed query in this function to enable code re-usuability.
def showQueryResult(sql):
    # This code creates an in-memory table called 'Inventory'.
    engine     = create_engine('sqlite://', echo=False)
    connection = engine.connect()
    df.to_sql(name='Inventory', con=connection, if_exists='replace', index=False)

    # This code performs the query.
    queryResult = pd.read_sql(sql, connection)
    return queryResult

# everything except 'Cadbury','Waterford Corp.')
SQL = "SELECT * FROM Inventory WHERE vendor NOT IN('Cadbury','Waterford Corp.')"
results = showQueryResult(SQL)
print(results)
print('\n')
# only 'Cadbury','Waterford Corp.')
SQL = "SELECT * FROM Inventory WHERE vendor IN('Cadbury','Waterford Corp.')"
results = showQueryResult(SQL)
print(results)




# Example 12:
# Alias
import pandas as pd
PATH = "C:/"
CSV_DATA = "retailerDB.csv"
df = pd.read_csv(PATH + CSV_DATA)

def showQueryResult(sql):
    engine = create_engine('sqlite://', echo=False)
    connection = engine.connect()
    df.to_sql(name='Inventory', con=connection, if_exists='replace', index=False)

    queryResult = pd.read_sql(sql, connection)
    return queryResult

SQL = "SELECT productName || '-' || vendor AS ProductVendor  FROM Inventory"
results = showQueryResult(SQL)
print(results)



# Exercise 15
import pandas as pd
PATH = "C:/"
CSV_DATA = "retailerDB.csv"
df = pd.read_csv(PATH + CSV_DATA)

def showQueryResult(sql):
    engine     = create_engine('sqlite://', echo=False)
    connection = engine.connect()
    df.to_sql(name='Inventory', con=connection, if_exists='replace', index=False)

    queryResult = pd.read_sql(sql, connection)
    return queryResult

SQL = "SELECT productName,price, price*0.7 AS afterTaxPrice FROM Inventory"
results = showQueryResult(SQL)
print(results)










# Exercise 16
import pandas as pd
PATH = "C:/"
CSV_DATA = "retailerDB.csv"
df = pd.read_csv(PATH + CSV_DATA)

def showQueryResult(sql):
    engine     = create_engine('sqlite://', echo=False)
    connection = engine.connect()
    df.to_sql(name='Inventory', con=connection, if_exists='replace', index=False)

    queryResult = pd.read_sql(sql, connection)
    return queryResult

SQL = "SELECT vendor,productName FROM Inventory WHERE vendor LIKE '%ry'"
results = showQueryResult(SQL)
print(results)






# Exercise 17
import pandas as pd
PATH = "C:/"
CSV_DATA = "retailerDB.csv"
df = pd.read_csv(PATH + CSV_DATA)

def showQueryResult(sql):

    engine     = create_engine('sqlite://', echo=False)
    connection = engine.connect()
    df.to_sql(name='Inventory', con=connection, if_exists='replace', index=False)


    queryResult = pd.read_sql(sql, connection)
    return queryResult

SQL = "SELECT vendor,productName FROM Inventory WHERE productName LIKE 'F%'"
results = showQueryResult(SQL)
print(results)





# Exercise 18
import pandas as pd

PATH = "C:/"
CSV_DATA = "retailerDB.csv"
df = pd.read_csv(PATH + CSV_DATA)

def showQueryResult(sql):
    engine     = create_engine('sqlite://', echo=False)
    connection = engine.connect()
    df.to_sql(name='Inventory', con=connection, if_exists='replace', index=False)

    queryResult = pd.read_sql(sql, connection)
    return queryResult

SQL = "SELECT productName, MAX(price)  FROM Inventory GROUP BY productName"
results = showQueryResult(SQL)
print(results)
print('\n')
SQL = "SELECT productID, MAX(price)  FROM Inventory GROUP BY productID"
results = showQueryResult(SQL)
print(results)




# Exercise 19
import pandas as pd
from sqlalchemy import create_engine
PATH = "C:/"
CSV_DATA = "retailerDB.csv"
df = pd.read_csv(PATH + CSV_DATA)

def showQueryResult(sql):

    engine = create_engine('sqlite://', echo=False)
    connection = engine.connect()
    df.to_sql(name='Inventory', con=connection, if_exists='replace', index=False)
    queryResult = pd.read_sql(sql, connection)
    return queryResult

SQL = "SELECT vendor, SUM(quantity) AS TotalItemsStocked  FROM Inventory GROUP BY vendor HAVING vendor IN( 'Cadbury' , 'Waterford Corp.') "
results = showQueryResult(SQL)
print(results)



# Exercise 20
import pandas as pd
from sqlalchemy import create_engine
PATH = "C:/"
CSV_DATA = "retailerDB.csv"
df = pd.read_csv(PATH + CSV_DATA)

def showQueryResult(sql):

    engine = create_engine('sqlite://', echo=False)
    connection = engine.connect()
    df.to_sql(name='Inventory', con=connection, if_exists='replace', index=False)
    queryResult = pd.read_sql(sql, connection)
    return queryResult

SQL = "SELECT vendor, SUM(price*quantity) AS revenueValue  FROM Inventory GROUP BY vendor HAVING vendor IN( 'Silverware Inc.' , 'Waterford Corp.') "
results = showQueryResult(SQL)
print(results)







# Exercise 3
def displayContent(x):
    a = 25 # The number is born here.
    print('Inside the function the variable \'a\'=' + str(a))
    print('The parameter x=' + str(x))
    return # Locally declared variables die here when the function exits.

a = 100
displayContent(a)
print("The global value for \'a\'=" + str(a))




# Exercise 2
def convertStringToFloat(numerator, denominator):
    firstName = 'Azarm'
    print(firstName)
    def lastName(lastName):
        lastName = lastName
        print(lastName)
        breakpoint()
    try:
        result = numerator / denominator
        return result
    except Exception as e:
        return None
# your code goes here.
def showResult(result):
    if (result != None):
        print("The value is " + str(result))
    else:
        print("An error occurred during the division.")

result = convertStringToFloat(15, 5)
showResult(result)
print("")
result = convertStringToFloat(15, 0)
showResult(result)

