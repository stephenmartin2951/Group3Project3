import visualizations as vis
import utils as utl
import pandas as pd

#Create Issue DataFrames
PaperIssuesDF = vis.createDataFrame('issues/PaperMCPaperIssues.csv')
BakkesIssuesDF = vis.createDataFrame('issues/bakkesmodorgBakkesModSDKIssues.csv')

#Create Size DataFrames
PaperSizeDF = vis.createDataFrame('size/PaperMCPaperSize.csv')
BakkesSizeDF = vis.createDataFrame('size/bakkesmodorgBakkesModSDKSize.csv')

#Add Year
PaperIssuesDF = utl.addYear(PaperIssuesDF, 'Created_At', 'Year')
BakkesIssuesDF = utl.addYear(BakkesIssuesDF, 'Created_At', 'Year')
PaperSizeDF = utl.addYear(PaperSizeDF, 'Date', 'Year')
BakkesSizeDF = utl.addYear(BakkesSizeDF, 'Date', 'Year')

#Group By Year
commitTime = PaperIssuesDF['Year']
frequencyPerPeriod = commitTime.value_counts()
PaperIssuesDF = pd.DataFrame(frequencyPerPeriod).sort_index().reset_index()
PaperIssuesDF.columns = ['Year', 'Issues']
commitTime = BakkesIssuesDF['Year']
frequencyPerPeriod = commitTime.value_counts()
BakkesIssuesDF = pd.DataFrame(frequencyPerPeriod).sort_index().reset_index()
BakkesIssuesDF.columns = ['Year', 'Issues']
PaperSizeDF = PaperSizeDF.groupby(["Year"], as_index=False).mean()
BakkesSizeDF = BakkesSizeDF.groupby(["Year"], as_index=False).mean()

Years = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

paperIssuesDensity = pd.DataFrame()
bakkesIssuesDensity = pd.DataFrame()

#For year in years, add issues and size


print(paperIssuesDensity)