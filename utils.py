import pandas as pd

def addMonth(df, dateFieldBeingConverted, newFieldName):
    df[newFieldName] = pd.to_datetime(df[dateFieldBeingConverted]).dt.month
    return df

def addYear(df, dateFieldBeingConverted, newFieldName):
    df[newFieldName] = pd.to_datetime(df[dateFieldBeingConverted]).dt.year
    return df

def frequencyPerDate(df, dateField, metric):
    commitTime = pd.DataFrame(df[dateField])
    frequencyPerPeriod = commitTime[dateField].value_counts()
    valCounts = pd.DataFrame(frequencyPerPeriod).sort_index().reset_index()
    valCounts.columns = [dateField, metric]
    # Returns the data frame with only year and number of commits for that time period
    return valCounts