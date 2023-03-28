import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import utils as utl



def createDataFrame(filePath):
    return pd.read_csv(filePath, header = 0)

def createScatterPlot(df, xAxis, yAxis, color, xAxisTitle = "x Axis" , yAxisTitle = "y Axis", chartTitle = "Chart Title"):
    df.plot.scatter(x = xAxis, y = yAxis, c = color)
    plt.ylabel(yAxisTitle)
    plt.xlabel(xAxisTitle)
    plt.title(chartTitle)
    plt.show()

#Comparing two repos
def createScatterPlot(df, xAxis, yAxis, color, df2, color2, xAxisTitle = "x Axis" , yAxisTitle = "y Axis", chartTitle = "Chart Title"):
    df.plot.scatter(x = xAxis, y = yAxis, c = color)
    df2.plot.scatter(x = xAxis, y = yAxis, c = color2)
    plt.ylabel(yAxisTitle)
    plt.xlabel(xAxisTitle)
    plt.title(chartTitle)
    plt.show()    

def createBarChart(df, xAxis, yAxis, xAxisTitle = "x Axis" , yAxisTitle = "y Axis", chartTitle = "Chart Title"):
    df.plot.bar(x=xAxis, y=yAxis)
    plt.ylabel(yAxisTitle)
    plt.xlabel(xAxisTitle)
    plt.title(chartTitle)
    plt.show() 

#Comparing two repos       
def createBarChart(df, xAxis, yAxis, df2, xAxisTitle = "x Axis" , yAxisTitle = "y Axis", chartTitle = "Chart Title"):
    df.plot.bar(x=xAxis, y=yAxis)
    df2.plot.bar(x=xAxis, y=yAxis)
    plt.ylabel(yAxisTitle)
    plt.xlabel(xAxisTitle)
    plt.title(chartTitle)
    plt.show() 

#Create DataFrames
df = createDataFrame('issues/PaperMCPaperIssues.csv')
df2 = createDataFrame('issues/bakkesmodorgBakkesModSDKIssues.csv')

#Add a column that contains the Created_At year and call the column "Created_At_Year"
utl.addYear(df, 'Created_At', 'Created_At_Year')
utl.addYear(df2, 'Created_At', 'Created_At_Year')

#Aggregate DataFrames by year values
aggDF = utl.frequencyPerDate(df, 'Created_At_Year', "Comments")
aggDF2 = utl.frequencyPerDate(df2, 'Created_At_Year', "Comments")


createScatterPlot(df, 'Created_At', 'Comments', 'DarkBlue', df2, "Green", "Created at Date", "Number of Comments", "Comments over Time")
createBarChart(aggDF, 'Created_At_Year', 'Comments', aggDF2, "Years", "Number of Comments", "Comments per Year")