import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import utils as utl

def createDataFrame(filePath):
    return pd.read_csv(filePath, header = 0)

def createScatterPlot(df, xAxis, yAxis, color, xAxisTitle = "x Axis" , yAxisTitle = "y Axis", chartTitle = "Chart Title", save = False, fileName = "", savePath = ""):
    df.plot.scatter(x = xAxis, y = yAxis, c = color)
    plt.ylabel(yAxisTitle)
    plt.xlabel(xAxisTitle)
    plt.title(chartTitle)
    if(save):
        plt.savefig('{}/{}'.format(savePath, fileName))
    else:
        plt.show() 

def createBarChart(df, xAxis, yAxis, xAxisTitle = "x Axis" , yAxisTitle = "y Axis", chartTitle = "Chart Title", save = False, fileName = "", savePath = ""):
    df.plot.bar(x=xAxis, y=yAxis)
    plt.ylabel(yAxisTitle)
    plt.xlabel(xAxisTitle)
    plt.title(chartTitle)
    if(save):
        plt.savefig('{}/{}'.format(savePath, fileName))
    else:
        plt.show()  

def createDoubleBarChart(xAxis1Name, xAxis1, xAxis2Name, xAxis2, DFindex, xAxisTitle = "x Axis" , yAxisTitle = "y Axis", chartTitle = "Chart Title", save = False, fileName = "", savePath = ""):
    barChartDF = pd.DataFrame({xAxis1Name: xAxis1, xAxis2Name: xAxis2}, index=DFindex)
    barChartDF.plot.bar(rot=0)
    plt.ylabel(yAxisTitle)
    plt.xlabel(xAxisTitle)
    plt.title(chartTitle)
    if(save):
        plt.savefig('{}/{}'.format(savePath, fileName))
    else:
        plt.show() 

def createLineChart(df, xAxis, yAxis, xAxisTitle = "x Axis" , yAxisTitle = "y Axis", chartTitle = "Chart Title", save = False, fileName = "", savePath = ""):
    df.plot.line(x=xAxis, y=yAxis)
    plt.ylabel(yAxisTitle)
    plt.xlabel(xAxisTitle)
    plt.title(chartTitle)
    if(save):
        plt.savefig('{}/{}'.format(savePath, fileName))
    else:
        plt.show()          

