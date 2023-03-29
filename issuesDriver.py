import visualizations as vis
import utils as utl


#Create Issue DataFrames
PaperIssuesDF = vis.createDataFrame('issues/PaperMCPaperIssues.csv')
BakkesIssuesDF = vis.createDataFrame('issues/bakkesmodorgBakkesModSDKIssues.csv')

#Create separate DFs for open and closed issues
PaperOpenIssuesDF = PaperIssuesDF.loc[PaperIssuesDF['State'] == 'open']
PaperClosedIssuesDF = PaperIssuesDF.loc[PaperIssuesDF['State'] == 'closed']
BakkesOpenIssuesDF = BakkesIssuesDF.loc[BakkesIssuesDF['State'] == 'open']
BakkesClosedIssuesDF = BakkesIssuesDF.loc[BakkesIssuesDF['State'] == 'closed']

#Add Years
utl.addYear(PaperOpenIssuesDF, 'Created_At', 'Created_At_Year')
utl.addYear(PaperClosedIssuesDF, 'Created_At', 'Created_At_Year')
utl.addYear(BakkesOpenIssuesDF, 'Created_At', 'Created_At_Year')
utl.addYear(BakkesClosedIssuesDF, 'Created_At', 'Created_At_Year')

#Summarize by years
aggPaperOpenIssuesDF = utl.frequencyPerDate(PaperOpenIssuesDF, 'Created_At_Year', 'State')
aggPaperClosedIssuesDF = utl.frequencyPerDate(PaperClosedIssuesDF, 'Created_At_Year', 'State')
aggBakkesOpenIssuesDF = utl.frequencyPerDate(BakkesOpenIssuesDF, 'Created_At_Year', 'State')
aggBakkesClosedIssuesDF = utl.frequencyPerDate(BakkesClosedIssuesDF, 'Created_At_Year', 'State')

Years = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

# print(aggPaperOpenIssuesDF['State'])
# print(aggPaperClosedIssuesDF['State'])

# vis.createDoubleBarChart(aggPaperOpenIssuesDF, aggPaperClosedIssuesDF, 'Open', 'State', 'Closed', 'State',
#                           [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023], 'Years', 'Number of Issues','Open & Closed Issues per Year' )