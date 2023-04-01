import pandas as pd
import numpy as np

def addMonth(df, dateFieldBeingConverted, newFieldName):
    df[newFieldName] = pd.to_datetime(df[dateFieldBeingConverted]).dt.month
    return df

def addYear(df, dateFieldBeingConverted, newFieldName):
    df[newFieldName] = pd.to_datetime(df[dateFieldBeingConverted]).dt.year
    return df

def addDate(df, dateFieldBeingConverted, newFieldName):
    df[newFieldName] = pd.to_datetime(df[dateFieldBeingConverted]).dt.date
    return df

def addDaysToClose(df, createdDate, closedDate):
    df["Days_to_Close"] = (pd.to_datetime(df[closedDate]) - pd.to_datetime(df[createdDate])) / np.timedelta64(1, 'D')
    return df

#Datefield = date value to aggregate by, metric = metric to aggregate
def frequencyPerDate(df, dateField, metric):
    commitTime = pd.DataFrame(df[dateField])
    frequencyPerPeriod = commitTime[dateField].value_counts()
    valCounts = pd.DataFrame(frequencyPerPeriod).sort_index().reset_index()
    valCounts.columns = [dateField, metric]
    # Returns the data frame with only year and number of commits for that time period
    return valCounts