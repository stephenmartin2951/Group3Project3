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

paperOpenIssuesYearlyTotal, paperClosedIssuesYearlyTotal, bakkesOpenIssuesYearlyTotal, bakkesClosedIssuesYearlyTotal = ([] for i in range(4))

for year in Years:
    try:    
        paperOpenIssuesYearlyTotal.append(aggPaperOpenIssuesDF.loc[aggPaperOpenIssuesDF['Created_At_Year'] == year]['State'].values[0])
    except IndexError:
        paperOpenIssuesYearlyTotal.append(0)
    try:    
        paperClosedIssuesYearlyTotal.append(aggPaperClosedIssuesDF.loc[aggPaperClosedIssuesDF['Created_At_Year'] == year]['State'].values[0])
    except IndexError:
        paperClosedIssuesYearlyTotal.append(0) 
    try:    
        bakkesOpenIssuesYearlyTotal.append(aggBakkesOpenIssuesDF.loc[aggBakkesOpenIssuesDF['Created_At_Year'] == year]['State'].values[0])
    except IndexError:
        bakkesOpenIssuesYearlyTotal.append(0) 
    try:    
        bakkesClosedIssuesYearlyTotal.append(aggBakkesClosedIssuesDF.loc[aggBakkesClosedIssuesDF['Created_At_Year'] == year]['State'].values[0])
    except IndexError:
        bakkesClosedIssuesYearlyTotal.append(0)         


vis.createDoubleBarChart('Open', paperOpenIssuesYearlyTotal, 'Closed', paperClosedIssuesYearlyTotal,
                          [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023], 'Years', 'Number of Issues','Open & Closed Issues per Year' )

vis.createDoubleBarChart('Open', bakkesOpenIssuesYearlyTotal, 'Closed', bakkesClosedIssuesYearlyTotal,
                          [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023], 'Years', 'Number of Issues','Open & Closed Issues per Year' )