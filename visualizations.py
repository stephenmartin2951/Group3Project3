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

def createDoubleBarChart(xAxis1Name, xAxis1, xAxis2Name, xAxis2, DFindex, xAxisTitle = "x Axis" , yAxisTitle = "y Axis", chartTitle = "Chart Title"):
    barChartDF = pd.DataFrame({xAxis1Name: xAxis1, xAxis2Name: xAxis2}, index=DFindex)
    barChartDF.plot.bar(rot=0)
    plt.ylabel(yAxisTitle)
    plt.xlabel(xAxisTitle)
    plt.title(chartTitle)
    plt.show() 

