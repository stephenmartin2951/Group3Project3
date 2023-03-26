import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def createDataFrame(filePath):
    return pd.read_csv(filePath, header = 0)

def createDateFreqDF(df):
    # Creates a data frame with JUST each year the repo was committed to and the # of commits for that year
    df['Years'] = pd.to_datetime(df['Commit Date']).dt.year
    commitYears = pd.DataFrame(df['Years'])
    countYears = commitYears['Years'].value_counts()
    valCounts = pd.DataFrame(countYears).sort_index().reset_index()
    valCounts.columns = ['Years', 'Frequency']
    # Returns the data frame with only
    return valCounts

def createBarChart(df):
    plottingDF = createDateFreqDF(df)
    plottingDF.plot.bar(x = 'Years', y = 'Frequency')
    plt.title('Commits per Year')
    plt.show()

def createScatterPlot(df):
    plottingDF = createDateFreqDF(df)
    plottingDF.plot(x = 'Years', y = 'Frequency')
    plt.ylabel('Number of Commits')
    plt.title('Commits per Year')
    plt.show()


paperCommitsDF = createDataFrame('commits/PaperMCPaperCommits.csv')

createBarChart(paperCommitsDF)
createScatterPlot(paperCommitsDF)