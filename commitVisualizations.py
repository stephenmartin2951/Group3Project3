import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def createDataFrame(filePath):
    return pd.read_csv(filePath, header = 0)

# TODO: Allow the user to specify what unit of time should be on x axis
def createDateFreqDF(df):
    # Creates a data frame with JUST each year the repo was committed to and the # of commits for that year
    df['Years'] = pd.to_datetime(df['Commit Date']).dt.year
    commitYears = pd.DataFrame(df['Years'])
    countYears = commitYears['Years'].value_counts()
    valCounts = pd.DataFrame(countYears).sort_index().reset_index()
    valCounts.columns = ['Years', 'Frequency']
    # Returns the data frame with only year and number of commits for that year
    return valCounts

def createBarChart(df, xAxis, yAxis):
    plottingDF = createDateFreqDF(df)
    plottingDF.plot.bar(x=xAxis, y=yAxis)
    plt.title('Commits per Year')
    plt.show()

def createScatterPlot(df, xAxis, yAxis, color):
    plottingDF = createDateFreqDF(df)
    plottingDF.plot(x=xAxis, y=yAxis, c=color)
    plt.ylabel('Number of Commits')
    plt.title('Commits per Year')
    plt.show()


paperCommitsDF = createDataFrame('commits/PaperMCPaperCommits.csv')

createBarChart(paperCommitsDF, 'Years', 'Frequency')
createScatterPlot(paperCommitsDF, 'Years', 'Frequency', 'DarkBlue')