import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def createDataFrame(filePath):
    return pd.read_csv(filePath, header = 0)

def createScatterPlot(df, xAxis, yAxis, color):
    df.plot.scatter(x = xAxis, y = yAxis, c = color)
    plt.show()

#Comparing two repos
def createScatterPlot(df, xAxis, yAxis, color, df2, color2):
    df.plot.scatter(x = xAxis, y = yAxis, c = color)
    df2.plot.scatter(x = xAxis, y = yAxis, c = color2)
    plt.show()    


df = createDataFrame('issues/PaperMCPaperIssues.csv')
df2 = createDataFrame('issues/bakkesmodorgBakkesModSDKIssues.csv')

createScatterPlot(df, 'Created_At', 'Comments', 'DarkBlue', df2, "Green")