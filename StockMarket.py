# Azarm Piran| new version

# This application allows users to examine daily and cumulative changes to closing price and volume for stocks in the stock market.
import pandas_datareader as pdr
import datetime
import pandas as pd
import pandas as pd
pd.options.mode.chained_assignment = None
#default='warn'

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# The application prompts the user to either examine a stock or terminate the application.
# Option menu function
def menuFunction():
    print('-------------------------------------------------')
    print('Stock Report Menu Options')
    print('-------------------------------------------------')
    print('1. Report changes for a stock')
    print('2. Quit')
    menu = input()
    if menu == str(1):
        mainFunction()
        menuFunction()
    elif menu == str(2):
        print('You quit')
    else:
        print('Your response is not recognized. Please try again.')
        menuFunction()

# I am using 3 functions in the mainFunction. The first part is asking for the stock symbol.
# Main function
def mainFunction():
    print('Please enter the stock symbol:')
    symbol = input()
    print(symbol)
    while True:
        try:
            numberOfDays = int(input("Please enter the number of days for the analysis:"))
            print(numberOfDays)
            break
        except ValueError:
            print('Oops!  That was no valid number.  Try again...')
            print('-------------------------------------------------')
            print('\n')
    dt = datetime.date.today()
    dtPast = dt - datetime.timedelta(days= int(numberOfDays)) + datetime.timedelta(days= 1)
    print('**************************************************')
    print(f'Daily Percent Changes - {dtPast} to {dt} * {symbol} * ')
    print('**************************************************')
    def getStock(stk,day):
        dt = datetime.date.today()
        dtPast = dt - datetime.timedelta(days= int(day)) + datetime.timedelta(days= 1)
        df = pdr.get_data_yahoo(stk,
             start = datetime.datetime(dtPast.year, dtPast.month, dtPast.day),
             end  = datetime.datetime(dt.year, dt.month, dt.day))
        return df
    df = getStock(symbol,numberOfDays)
    numRows = len(df)
    # Deleting 3 columns that I do not need them in the output
    del df['High']
    del df['Low']
    del df['Open']
    del df['Adj Close']
    df['Volum % change'] = ''
    df['Close % change'] = ''

    # This function calculates the percent change price in the data frame. Last 2 columns of data frame
    def percentChangePriceCalculationFunction(df,column,base):
        if len(df) ==1:
            df[str(column)].iloc[0] = 0
        else:
            df[str(column)].iloc[0] = 0
            i = 1
            for i in range(1, len(df)):
                currentDayPrice = df.iloc[numRows - i][str(base)]
                previousDayPrice = df.iloc[numRows - i - 1][str(base)]
                dailyPercentChangePrice = ((currentDayPrice - previousDayPrice) / previousDayPrice)
                df[str(column)].iloc[len(df) - i] = dailyPercentChangePrice


    percentChangePriceCalculationFunction(df,'Close % change','Close')
    percentChangePriceCalculationFunction(df, 'Volum % change', 'Volume')

    print(df)
    print('-------------------------------------------------')
    print(f'Summary of Cumulative Changes for {symbol}')
    print('-------------------------------------------------')
    print(f'{dtPast} to {dt}')
    numRows = len(df)

    # This function calculates the volume price change and close price change
    def priceChangeFunction(df,column):
        periodEndPrice = df.iloc[numRows - 1][str(column)]
        periodStartPrice = df.iloc[0][str(column)]
        overallPercentageChangePrice = ((periodEndPrice - periodStartPrice) / periodStartPrice)
        return round(overallPercentageChangePrice,3)

    closePriceChange = priceChangeFunction(df,'Close')
    volumePriceChange = priceChangeFunction(df, 'Volume')

    print(f'% Volume Change: {volumePriceChange}')
    print(f'% Close Price Change: {closePriceChange}')



menuFunction()

