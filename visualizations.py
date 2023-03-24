import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def createDataFrame(filePath):
    return pd.read_csv(filePath, header = 0)

def createScatterPlot(df, xAxis, yAxis, color):
    df.plot.scatter(x = xAxis, y = yAxis, c = color)
    plt.show()


df = createDataFrame('issues/PaperMCPaperIssues.csv')

createScatterPlot(df, 'Created_At', 'Comments', 'DarkBlue')