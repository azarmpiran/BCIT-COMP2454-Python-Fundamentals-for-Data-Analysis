# This is InClass Week 2 Practice for COMP2454
# String Manipulation and DataFrames
# British Columbia Institute of Technology
# Azarm Piran





# Example 1
# Searches for match in an array of characters and starts count at 0.
sentence = "A lazy dog jumped over a log"
x = sentence.find('dog')
print(x)
print("Starting position: " + str(sentence.find('dog')))
# When item not found -1 is returned.
sentence = "A lazy dog jumped over a log"
print("Starting position: " + str(sentence.find('cat')))



# Example 2
# Obtaining Substrings
fullName = "Bob Jones"
spacePosition = fullName.find(" ")
print(spacePosition)
startPosition = 0
# First name ends where we have the first space
endPosition = spacePosition
# Here we see the full name as a array of strings
firstName = fullName[startPosition:endPosition]
print(firstName)
# Exercise 1
fullName = "Bob Jones"
fullNameLen = len(fullName)
print(fullNameLen)
lastName = fullName[spacePosition+1:fullNameLen]
print(lastName)



# Creating a function that receive a full name and gives a first name and last name separately
def fullNameFunction(fullName):
    firstSapcePosition = fullName.find(" ")
    fullNameLen = len(fullName)
    firstName = fullName[0:firstSapcePosition]
    lastName = fullName[firstSapcePosition+1:fullNameLen]
    print(firstName)
    print(lastName)
    print(f"Your First Name is {firstName} and Your Last Name is {lastName}.")

fullNameFunction("Azarm Piran")
fullNameFunction("Roya Saee")


# Example 3
# Finding Multiple Occurrences of a Substring
text = "A lazy dog jumped over a log."
# Here we create an array to save all the possible occurrences
positions = []
for i in range(0, len(text) - 1):
    if (text[i:i + 1] == "og"):
        # Here, for the first loop, we say 0:2 because it will not read the index 2. It will read index 0 and 1
        positions.append(i)

print(positions)



# Practice
# Saving each character individually in a array
sentence = "She sells seashells by the sea shore."
array =[]
for i in range(0, len(sentence)-1):
    array.append(sentence[i])
    i = i + 1

print(array)


# Practice
# Finding the location of all s in the text - S and s are different.
# It will not find S since in the if we are looking for s
sentence = "She sells seashells by the sea shore."
array = []
for i in range(0, len(sentence) - 1):
    if (sentence[i] == "s"):
        array.append(i)

print(array)



# Exercise 2
# Find the positions of ‘sea’ in the following sentence:
# “She sells seashells by the sea shore.”
sentence = "She sells seashells by the sea shore."
array = []
for i in range(0, len(sentence) - 1):
    if (sentence[i:i+3] == "sea"):
        array.append(i)
print(array)


# Exercise 2 as a function
def findLocationFunction(text,string,numberOfCharacter):
    sentence = text
    array = []
    for i in range(0, len(sentence) - 1):
        if (sentence[i:i + numberOfCharacter] == string):
            array.append(i)
    print(array)

findLocationFunction("Hello World","llo",3)
findLocationFunction("Hi my name is azarm azarm aza azarmpiran my first name is azarm","az",2)



# Replacing Strings
# Example 4
text = "A lazy dog jumped over a log."
newText = text.replace("dog", "cat")
print(newText)



# Exercise 3
text = "A lazy dog jumped over a log."
newText = text.replace("lazy dog","dog")
print(newText)



# Example 5
word = "A lazy dog jumped over a log."
sentenceArray = word.split(' ')
print(sentenceArray)

for counter in range(0, len(sentenceArray)):
    print(sentenceArray[counter])



# Example 6
sentenceArray = ['A', 'lazy', 'dog', 'jumped', 'over', 'a', 'log.']
delimiter     = ' '
newSentence   = delimiter.join(sentenceArray)
print(newSentence)



# Exercise 4
sentenceArray = ['A', 'lazy', 'dog', 'jumped', 'over', 'a', 'log.']
delimiter = ','
newSentence = delimiter.join(sentenceArray)
print(newSentence)



# DataFrames
import pandas as pd
# Create data set.
dataSet = {'First Name': ['Jonny','Holly','Nira'],
           'Grade': [85,95,91] }
# Create dataframe with data set and named columns.
# Column names must match the dataSet properties.
df = pd.DataFrame(dataSet, columns= ['First Name', 'Grade'])
# Show DataFrame
print(df)



# Exercise 5
import pandas as pd
dataSet = { 'First Name': ['Jonny','Holly','Nira'],
            'Last Name': ['Staub','Conway ','Arora'],
            'Grade': [85,95,91]
}
df = pd.DataFrame(dataSet, columns= ['First Name', 'Last Name','Grade'])
print(df)



# Example 8
import pandas as pd
dataSet = {'Market': ['S&P 500', 'Dow', 'Nikkei'],
           'Last': [2932.05, 26485.01, 21087.16] }
df = pd.DataFrame(dataSet, columns= ['Market', 'Last'])
print("\n*** Original DataFrame ***")
print(df)
# Create change column.
change = [-21.51, -98.41, -453.83]

# Append change column.
df['Change'] = change
print("\n*** Adjusted DataFrame ***")
print (df)



# Exericse 6
import pandas as pd
dataSet = { 'Market': ['S&P 500', 'Dow', 'Nikkei'],
            'Last':[2932.05, 26485.01, 21087.16],
            'change': [-21.51, -98.41, -453.83]
}
table = pd.DataFrame(dataSet, columns=['Market','Last','change'])
print("\n *** Here we can see our table***")
print(table)
percentageChange = [-0.73,-0.37,-2.11]
# Append
table['Percentage Change'] = percentageChange
print("\n *** Here we can see our table***")
print(table)
print(table.loc[0]['Last'])


#Example 9
import pandas as pd
# Create data set.
dataSet = {'Market': ['S&P 500', 'Dow', 'Nikkei'],
           'Last': [2932.05, 26485.01, 21087.16] }
# Create dataframe with data set and named columns.
df = pd.DataFrame(dataSet, columns= ['Market', 'Last'])
# Show original DataFrame.
print("\n*** Original DataFrame ***")
print(df)
# Add new line.
print("\n")
# Show names only
for i in range(len(df)):
    print(df.loc[i]['Market'])



# Exercise 7
import pandas as pd
dataSet = { 'Market': ['S&P 500', 'Dow', 'Nikkei'],
            'Last': [2932.05, 26485.01, 21087.16]
}

df = pd.DataFrame(dataSet,columns= ['Market','Last'])
print('\nHere is the whole data set:')
print(df)
print('\nOnly second column:')
for i in range(0,len(df)):
    print(df.loc[i]['Last'])



# Exercise 8
import pandas as pd
dataSet = { 'Market': ['S&P 500', 'Dow', 'Nikkei'],
            'Last': [2932.05, 26485.01, 21087.16]
}

df = pd.DataFrame(dataSet,columns= ['Market','Last'])
print('\nHere is the whole data set:')
print(df)
print('\nMethod 1 to show only first row:')
print(df.loc[0])
print('\nMethod 2 to show only first row:')
print(df.iloc[0])



# Example 10
import pandas as pd
# Create data set.
dataSet = {'Market': ['S&P 500', 'Dow', 'Nikkei'],
           'Last': [2932.05, 26485.01, 21087.16] }

# Create dataframe with data set and named columns.
df1 = pd.DataFrame(dataSet, columns= ['Market', 'Last'])
# Show original DataFrame.
print("\n*** Original DataFrame ***")
print(df1)
dataSet2 = { 'Market': ['Hang Seng', 'DAX'],
             'Last': [26918.58, 11872.44]}
df2 = pd.DataFrame(dataSet2, columns= ['Market', 'Last'])
df1 = df1.append(df2)
print("\n*** New version DataFrame ***")
print(df1)



# Exercise 9
import pandas as pd
dataSet1 = {'Market':['S&P 500', 'Dow', 'Nikkei'],
           'Last':[2932.05, 26485.01, 21087.16]
}
df1 = pd.DataFrame(dataSet, columns=['Market','Last'])
print('\nFirst DataFrame:')
print(df1)
dataSet2 = { 'Market':['Hang Seng', 'DAX'],
             'Last':[26918.58, 11872.44]
}
df2 = pd.DataFrame(dataSet2, columns=['Market','Last'])
print('\nSecond DataFrame:')
print(df2)
print('\nFirst AND Second DataFrame:')
df = df1.append(df2)
print(df)
dataSet3 = {'Market':['FTSE100'],
            'Last':[7407.06]

}
df3 = pd.DataFrame(dataSet3, columns=['Market','Last'])
print('\nThird DataFrame:')
print(df3)
df = df.append(df3)
print('\nFirst AND Second AND Third DataFrame all together:')
print(df)



# Dictionaries
# Appending dictionaries to DataFrames
# Example 11
import pandas as pd
# Create data set.
dataSet = {'Market': ['S&P 500', 'Dow'],
           'Last': [2932.05, 26485.01]}

# The dictionary is an object made of name value pairs.
stockDictionary = {'Market': 'Nikkei', 'Last': 21087.16 }
# Create dataframe with data set and named columns.
df = pd.DataFrame(dataSet, columns= ['Market', 'Last'])
# Show original DataFrame.
print("\n*** Original DataFrame ***")
print(df)
df = df.append(stockDictionary, ignore_index=True)
print('\n')
print(df);



# Exercise 10
import pandas as pd
dataSet = {'Market': ['S&P 500', 'Dow'],
           'Last': [2932.05, 26485.01]

}
df = pd.DataFrame(dataSet, columns=['Market','Last'])
print('\nOriginal DataFrame:')
print(df)
dictionary = {'Market':'DAX','Last':11872.44}
df = df.append(dictionary,ignore_index=True)
print('\nDataFrame and Dictionary:')
print(df)



# Example 12
import pandas as pd

# Import data from a specific location into a DataFrame. Using pandas.read_table() function
path = "C:/babysamp-98.txt"
df = pd.read_table(path, skiprows=1,
                   delim_whitespace=True,
                   names=('MomAge', 'DadAge', 'MomEduc', 'MomMarital', 'numlive',
                          "dobmm", 'gestation', 'sex', 'weight', 'prenatalstart',
                          'orig.id', 'preemie'))
# Show all columns.
# The second input in set_option function refers to the number of columns that we will get in df
pd.set_option('display.max_columns', None)
#print(df)
# Increase number of columns that display on one line.
pd.set_option('display.width', 1000)
print(df)
# Using head() function
print("\n FIRST 2 ROWS") # Prints title with space before.
print(df.head(2))

# Using tail function
print("\n LAST 2 ROWS")
print(df.tail(2))

# Show data types for each columns.
print("\n DATA TYPES") # Prints title with space before.
print(df.dtypes)

# Show statistical summaries for numeric columns.
print("\nSTATISTIC SUMMARIES for NUMERIC COLUMNS")
print(df.describe())

# Show summaries for objects like dates and strings.
print("\nSTATISTIC SUMMARIES for DATE and STRING COLUMNS")
print(df.describe(include=['object']))



# Exercise 11
import pandas as pd
path = "C:/bodyfat.txt"
df = pd.read_csv(path, skiprows=1,
                   sep='\t',
                   names=('Density', 'Pct.BF', 'Age',   'Weight', 'Height',
                           'Neck', 'Chest', 'Abdomen',  'Waist', 'Hip',  'Thigh',
                          'Ankle', 'Knee', 'Bicep', 'Forearm', 'Wrist'))
# Show all columns.
pd.set_option('display.max_columns', None)
print(df)

# Increase number of columns that display on one line.
pd.set_option('display.width', 1000)
print(df)

# First 2 rows
print('\nFirst 2 rows:')
print(df.head(2))

# Last 2 rows
print('\nLast 2 rows:')
print(df.tail(2))

# Datatype of the dataFrame
print('\nData type of the data:')
print(df.dtypes)

# Data summaries
print('\nData Summary:')
print(df.describe().round(2))


# Example 13
# Extracting Column Subsets
import pandas as pd
# Create data set.
dataSet = {'Market': ['S&P 500', 'Dow', 'Nikkei'],
           'Last': [2932.05, 26485.01, 21087.16] }

# Create dataframe with data set and named columns.
df = pd.DataFrame(dataSet, columns= ['Market', 'Last'])
change = [-21.51, -98.41, -453.83]

df['Change'] = change

df2 = df[["Market", "Change"]]
# Show DataFrame
print("\n*** Adjusted DataFrame ***")
print (df2)


# Exercise 12
import pandas as pd
path = "C:/bodyfat.txt"
df = pd.read_csv(path, skiprows=1,
                   sep='\t',
                   names=('Density', 'Pct.BF', 'Age',   'Weight', 'Height',
                           'Neck', 'Chest', 'Abdomen',  'Waist', 'Hip',  'Thigh',
                          'Ankle', 'Knee', 'Bicep', 'Forearm', 'Wrist'))

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print(df)

df2 = df[['Height','Waist','Weight','Pct.BF']]
print('\nAdjusted DataFrame:')
print(df2)

print('\nFirst row of adjusted dataFrame:')
print(df2.head(1))


# Example 14
# Changing Column Names
import pandas as pd
import matplotlib.pyplot as plt
# Import data into a DataFrame.
path = "C:/babysamp-98.txt"
df = pd.read_csv(path, skiprows=1,
                   sep='\t',
                   names=('MomAge', 'DadAge', 'MomEduc', 'MomMarital', 'numlive',
                          "dobmm", 'gestation', 'sex', 'weight', 'prenatalstart',
                          'orig.id', 'preemie'))

# Rename the columns so they are more reader-friendly.
df = df.rename({'MomAge': 'Mom Age', 'DadAge':'Dad Age',
                'MomEduc':'Mom Edu', 'weight':'Weight'}, axis=1)  # new method
# Show all columns.
pd.set_option('display.max_columns', None)

# Increase number of columns that display on one line.
pd.set_option('display.width', 1000)
print(df.head())


# Exercise 13
import pandas as pd
path = "C:/bodyfat.txt"
df = pd.read_csv(path, skiprows=1,
                   sep='\t',
                   names=('Density', 'Pct.BF', 'Age',   'Weight', 'Height',
                           'Neck', 'Chest', 'Abdomen',  'Waist', 'Hip',  'Thigh',
                          'Ankle', 'Knee', 'Bicep', 'Forearm', 'Wrist'))

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print(df)

df2 = df[['Height','Waist','Weight','Pct.BF']]
print('\nAdjusted DataFrame:')
print(df2)
df2 = df2.rename({'Pct.BF':'Percent Body Fat'}, axis=1)
print(df2)



# Frequencies and Ranges
# Example 15
import pandas as pd
import matplotlib.pyplot as plt

path = "C:/babysamp-98.txt"
df = pd.read_csv(path, skiprows=1,
                   sep='\t',
                   names=('MomAge', 'DadAge', 'MomEduc', 'MomMarital', 'numlive',
                          "dobmm", 'gestation', 'sex', 'weight', 'prenatalstart',
                          'orig.id', 'preemie'))

df = df.rename({'MomAge': 'Mom Age', 'DadAge':'Dad Age',
                'MomEduc':'Mom Edu', 'weight':'Weight'}, axis=1)  # new method

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print(df.head())
print("\nTOP FREQUENCY FIRST")
print(df['Mom Age'].value_counts())

print("\nLOWEST FREQUENCY FIRST")
print(df['Mom Age'].value_counts(ascending=True))

print("\nFREQUENCY SORTED by MOTHER AGE")
print(df['Mom Age'].value_counts().sort_index())



# Exercise 14
import pandas as pd
import matplotlib.pyplot as plt

path = "C:/babysamp-98.txt"
df = pd.read_csv(path, skiprows=1,
                   sep='\t',
                   names=('MomAge', 'DadAge', 'MomEduc', 'MomMarital', 'numlive',
                          "dobmm", 'gestation', 'sex', 'weight', 'prenatalstart',
                          'orig.id', 'preemie'))

df = df.rename({'MomAge': 'Mom Age', 'DadAge':'Dad Age',
                'MomEduc':'Mom Edu', 'weight':'Weight'}, axis=1)  # new method

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print(df.head())
print("\nFrequency Count of Unique Values for Mother Education:  TOP FREQUENCY FIRST")
print(df['Mom Edu'].value_counts())

print("\nFrequency Count of Unique Values for Mother Education:  LOWEST FREQUENCY FIRST")
print(df['Mom Edu'].value_counts(ascending=True))

print("\nFrequency Count of Unique Values for Mother Education:  FREQUENCY SORTED by MOTHER Education Level")
print(df['Mom Edu'].value_counts().sort_index())



# Example 16:
# Sorting DataFrame Content
import pandas as pd
import matplotlib.pyplot as plt
# Import data into a DataFrame.
path = "C:/babysamp-98.txt"
df = pd.read_csv(path, skiprows=1,
                   sep='\t',
                   names=('MomAge', 'DadAge', 'MomEduc', 'MomMarital', 'numlive',
                          "dobmm", 'gestation', 'sex', 'weight', 'prenatalstart',
                          'orig.id', 'preemie'))

# Rename the columns so they are more reader-friendly.
df = df.rename({'MomAge': 'Mom Age', 'DadAge':'Dad Age',
                'MomEduc':'Mom Edu', 'weight':'Weight'}, axis=1)  # new method
# Show all columns.
pd.set_option('display.max_columns', None)

# Increase number of columns that display on one line.
pd.set_option('display.width', 1000)

# Sort by descending mother age and then by ascending weight.
dfSorted = df.sort_values(['Mom Age', 'Weight'], ascending=[False, True])
print(dfSorted)



# Exercise 15
import pandas as pd
import matplotlib.pyplot as plt
# Import data into a DataFrame.
path = "C:/babysamp-98.txt"
df = pd.read_csv(path, skiprows=1,
                   sep='\t',
                   names=('MomAge', 'DadAge', 'MomEduc', 'MomMarital', 'numlive',
                          "dobmm", 'gestation', 'sex', 'weight', 'prenatalstart',
                          'orig.id', 'preemie'))

# Rename the columns so they are more reader-friendly.
df = df.rename({'MomAge': 'Mom Age', 'DadAge':'Dad Age',
                'MomEduc':'Mom Edu', 'weight':'Weight'}, axis=1)  # new method
# Show all columns.
pd.set_option('display.max_columns', None)

# Increase number of columns that display on one line.
pd.set_option('display.width', 1000)

# Sort by descending mother age and then by ascending weight.
dfSorted = df.sort_values(['gestation', 'Weight'], ascending=[True, True])
print(dfSorted)




# Example 17:
# Filtering with Compound Conditions
import matplotlib.pyplot as plt
import pandas as pd
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
# Compound conditions require single '&' for 'AND' and single '|' for 'OR.
resultDf = df[(df['DadAge']>=40) & (df['MomAge'] >= 40)]
print(resultDf)



# Exercise 16
import pandas as pd
import matplotlib.pyplot as plt

# Import data into a DataFrame.
path = "C:/babysamp-98.txt"
df = pd.read_csv(path, skiprows=1,
                   sep='\t',
                   names=('MomAge', 'DadAge', 'MomEduc', 'MomMarital', 'numlive',
                          "dobmm", 'gestation', 'sex', 'weight', 'prenatalstart',
                          'orig.id', 'preemie'))

# Rename the columns so they are more reader-friendly.
df = df.rename({'MomAge': 'Mom Age', 'DadAge':'Dad Age',
                'MomEduc':'Mom Edu', 'weight':'Weight'}, axis=1)  # new method
# Show all columns.
pd.set_option('display.max_columns', None)

# Increase number of columns that display on one line.
pd.set_option('display.width', 1000)
print(df.head())
df2 = df['Mom Age']
print('\nData Summary:')
print(df2.describe().round(3))



# Example 18:
# Grouping Summaries
import pandas as pd

# The data file path and file name need to be configured.
PATH = "C:/"
CSV_DATA = "phone_data.csv"

# Note this has a comma separator.
df = pd.read_csv(PATH + CSV_DATA, skiprows=1, encoding="ISO-8859-1", sep=',',
                 names=('index', 'date', 'duration', 'item', 'month', 'network',
                        'network_type'))
# Get count of items per month.
dfStats = df.groupby('network')['index'] \
    .count().reset_index().rename(columns={'index': '# Calls'})
print(dfStats)

# Get duration mean for network groups and convert to DataFrame.
dfDurationMean = df.groupby('network')['duration'] \
    .mean().reset_index().rename(columns={'duration': 'Duration Mean'})

# Get duration max for network groups and convert to DataFrame.
dfDurationMax = df.groupby('network')['duration'] \
    .max().reset_index().rename(columns={'duration': 'Duration Max'})

# Append duration mean to stats matrix.
dfStats['Duration Mean'] = dfDurationMean['Duration Mean']

# Append duration max to stats matrix.
dfStats['Duration Max'] = dfDurationMax['Duration Max']
print(dfStats)



# Exercise 17
import pandas as pd
PATH = "C:/"
CSV_DATA = "phone_data.csv"
df = pd.read_csv(PATH + CSV_DATA, skiprows=1, encoding="ISO-8859-1", sep=',',
                 names=('index', 'date', 'duration', 'item', 'month', 'network',
                        'network_type'))
dfStats = df.groupby('network')['index'] \
    .count().reset_index().rename(columns={'index': '# Calls'})
print(dfStats)

# Get duration mean for network groups and convert to DataFrame.
dfDurationMean = df.groupby('network')['duration'] \
    .mean().reset_index().rename(columns={'duration': 'Duration Mean'})

dfDurationMax = df.groupby('network')['duration'] \
    .max().reset_index().rename(columns={'duration': 'Duration Max'})

dfDurationMin = df.groupby('network')['duration'] \
    .min().reset_index().rename(columns={'duration': 'Duration Min'})

dfDurationStd = df.groupby('network')['duration'] \
    .std().reset_index().rename(columns={'duration': 'Duration sd'})

dfStats['Duration Mean'] = dfDurationMean['Duration Mean']

dfStats['Duration Max'] = dfDurationMax['Duration Max']

dfStats['Duration Min'] = dfDurationMin['Duration Min']

dfStats['Duration sd'] = dfDurationStd['Duration sd']
print(dfStats)





# Exercise 18
import pandas as pd
PATH = "C:/"
CSV_DATA = "phone_data.csv"
df = pd.read_csv(PATH + CSV_DATA, skiprows=1, encoding="ISO-8859-1", sep=',',
                 names=('index', 'date', 'duration', 'item', 'month', 'network',
                        'network_type'))
dfStats = df.groupby('network_type')['index'] \
    .count().reset_index().rename(columns={'index': '# Calls'})
print(dfStats)

# Get duration mean for network groups and convert to DataFrame.
dfDurationMean = df.groupby('network_type')['duration'] \
    .mean().reset_index().rename(columns={'duration': 'Duration Mean'})

dfDurationMax = df.groupby('network_type')['duration'] \
    .max().reset_index().rename(columns={'duration': 'Duration Max'})

dfDurationMin = df.groupby('network_type')['duration'] \
    .min().reset_index().rename(columns={'duration': 'Duration Min'})

dfDurationStd = df.groupby('network_type')['duration'] \
    .std().reset_index().rename(columns={'duration': 'Duration sd'})

dfStats['Duration Mean'] = dfDurationMean['Duration Mean']

dfStats['Duration Max'] = dfDurationMax['Duration Max']

dfStats['Duration Min'] = dfDurationMin['Duration Min']

dfStats['Duration sd'] = dfDurationStd['Duration sd']
print(dfStats)



# Exercise 19
import matplotlib.pyplot as plt
import pandas as pd
# Import data into a DataFrame.
path = "C:/babysamp-98.txt"
df = pd.read_csv(path, skiprows=1,
                   sep='\t',
                   names=('MomAge', 'DadAge', 'MomEduc', 'MomMarital', 'numlive',
                          "dobmm", 'gestation', 'sex', 'weight', 'prenatalstart',
                          'orig.id', 'preemie'))
print(df)

# Max
Max = df.groupby('sex')['weight'] \
    .max().reset_index().rename(columns={'weight': 'Max'})
print(Max)

# Min
Min = df.groupby('sex')['weight'] \
    .min().reset_index().rename(columns={'weight': 'Min'})
print(Min)

# Mean
Mean = df.groupby('sex')['weight'] \
    .mean().reset_index().rename(columns={'weight': 'Mean'})
print(Mean)

print('\n')
dfStats = Max
dfStats['Min'] = Min['Min']
dfStats['Mean'] = Mean['Mean']
print(dfStats)



# Example 19:
# Generating a Calculated Column
import pandas as pd

# Create data set.
dataSet = { 'Fahrenheit': [85,95,91] }

# Create dataframe with data set and named columns.
# Column names must match the dataSet properties.
df = pd.DataFrame(dataSet, columns= ['Fahrenheit'])

df['Celsius'] = (df['Fahrenheit']-32)*5/9
# Show DataFrame
print(df)




# Exercise 20:
# Generating a Calculated Column
import pandas as pd

# Create data set.
dataSet = { 'Fahrenheit': [85,95,91] }

# Create dataframe with data set and named columns.
# Column names must match the dataSet properties.
df = pd.DataFrame(dataSet, columns= ['Fahrenheit'])

df['Celsius'] = (df['Fahrenheit']-32)*5/9
df['Kelvin'] = (df['Celsius']+273.15)
# Show DataFrame
print(df)




# Example 20:
# Grouping on Multiple Columns
import pandas as pd

# The data file path and file name need to be configured.
PATH = "C:/"
CSV_DATA = "phone_data.csv"

# Note this has a comma separator.
df = pd.read_csv(PATH + CSV_DATA, skiprows=1, encoding="ISO-8859-1", sep=',',
                 names=('index', 'date', 'duration', 'item', 'month', 'network',
                        'network_type'))

df2 = df.groupby(['network', 'item'])['duration'].mean().reset_index()
print(df2)



# Exercise 21:
import pandas as pd
PATH = "C:/"
CSV_DATA = "phone_data.csv"

# Note this has a comma separator.
df = pd.read_csv(PATH + CSV_DATA, skiprows=1, encoding="ISO-8859-1", sep=',',
                 names=('index', 'date', 'duration', 'item', 'month', 'network',
                        'network_type'))

df2 = df.groupby(['network_type', 'item'])['duration'].count().reset_index()
print(df2)



# Example 21:
# Updating on Data Frame Cell at a Time
import pandas as pd

# Define empty data frame structure.
df = pd.DataFrame(columns=['City', 'Temperature'])
print(df)
# Add rows of data.
df = df.append({'City':'Mumbai', 'Temperature':23.0}, ignore_index=True)
df = df.append({'City':'Beijing', 'Temperature':-11.0}, ignore_index=True)
print(df)

print("Data frame with original data in Celsius:")
print(df)
print('Key:::')
print(df.keys())
# Show all columns of the data frame.
# Inja dar vaqe ye function neveshtim ke behesh df midim va un column e k mikhad update she ro ham midim
# tu for e badi formul ro barash neveshtim , inja faqat un ravandi ro tarahi mikonim ke ru tamame khune haye un column e mored e nazar becharkhe
def getColumnPosition(df, columnName):
    columnList = list(df.keys())

    # Show all columns of the data frame in a list.
    print(columnList)
    columnPosition = 0
    for i in range(0, len(columnList)):
        if(columnList[i]==columnName):
            columnPosition = i
            break # Exit the loop.
    return columnPosition

# Update cell values - one at a time.
tempColumnPosition = getColumnPosition(df, "Temperature")

for i in range(0, len(df)):
    celsius = df.iloc[i]['Temperature']
    df.iat[i, tempColumnPosition] = celsius*9.0/5.0 + 32

print("\nDataframe after changed to Fahrenheit: ")
print(df)





# Exercise 22:
import pandas as pd
df = pd.DataFrame(columns=['City', 'Temperature'])
print(df)
df = df.append({'City':'Mumbai', 'Temperature':23.0}, ignore_index=True)
df = df.append({'City':'Beijing', 'Temperature':-11.0}, ignore_index=True)
print(df)
print("Data frame with original data in Celsius:")
print(df)
def getColumnPosition(df, columnName):
    columnList = list(df.keys())

    # Show all columns of the data frame in a list.
    print(columnList)
    columnPosition = 0
    for i in range(0, len(columnList)):
        if(columnList[i]==columnName):
            columnPosition = i
            print('\nColumn Position:')
            print(columnPosition)
            break # Exit the loop.
    return columnPosition

# Updating City Column
tempColumnPosition = getColumnPosition(df, "City")
for i in range(0, len(df)):
    df.iat[i, tempColumnPosition] = f'The city of {df.iat[i, tempColumnPosition]}'
print("\nDataframe after changing the City Column: ")
print(df)

# Updating Temp Column
tempColumnPosition = getColumnPosition(df, "Temperature")
for i in range(0, len(df)):
    celsius = df.iloc[i]['Temperature']
    df.iat[i, tempColumnPosition] = celsius*9.0/5.0 + 32

print("\nDataframe after changed to Fahrenheit: ")
print(df)




