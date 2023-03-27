import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def createDataFrame(filePath):
    return pd.read_csv(filePath, header = 0)

# TODO: Allow the user to specify what unit of time should be on x axis
def createDateFreqDF(df, xAxis):
    # Creates a data frame with JUST each year the repo was committed to and the # of commits for that time period
    if xAxis == 'Year':
        df[xAxis] = pd.to_datetime(df['Commit Date']).dt.year
    elif xAxis == 'Month':
        df[xAxis] = pd.to_datetime(df['Commit Date']).dt.month
    commitTime = pd.DataFrame(df[xAxis])
    frequencyPerPeriod = commitTime[xAxis].value_counts()
    valCounts = pd.DataFrame(frequencyPerPeriod).sort_index().reset_index()
    valCounts.columns = [xAxis, 'Frequency']
    # Returns the data frame with only year and number of commits for that time period
    return valCounts

def createBarChart(df, xAxis, yAxis):
    plottingDF = createDateFreqDF(df, xAxis)
    plottingDF.plot.bar(x=xAxis, y=yAxis)
    plt.title('Commits per {}'.format(xAxis))
    plt.show()

def createScatterPlot(df, xAxis, yAxis, color):
    plottingDF = createDateFreqDF(df, xAxis)
    plottingDF.plot(x=xAxis, y=yAxis, c=color)
    plt.ylabel('Number of Commits')
    plt.title('Commits per {}'.format(xAxis))
    plt.show()


paperCommitsDF = createDataFrame('commits/PaperMCPaperCommits.csv')

# You can now pass in either Month or Year as your x-axis and the program will adapt
createBarChart(paperCommitsDF, 'Year', 'Frequency')
createScatterPlot(paperCommitsDF, 'Year', 'Frequency', 'DarkBlue')
createScatterPlot(paperCommitsDF, 'Month', 'Frequency', 'DarkBlue')