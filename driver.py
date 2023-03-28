import visualizations as vis
import utils as utl


#Create Issue DataFrames
PaperIssuesDF = vis.createDataFrame('issues/PaperMCPaperIssues.csv')
BakkesIssuesDF = vis.createDataFrame('issues/bakkesmodorgBakkesModSDKIssues.csv')

#Create Commit DataFrames
PaperCommitsDF = vis.createDataFrame('commits/PaperMCPaperCommits.csv')
BakkesCommitsDF = vis.createDataFrame('commits/bakkesmodorgBakkesModSDKCommits.csv')

#Create Size DataFrames
PaperSizeDF = vis.createDataFrame('size/PaperMCPaperSize.csv')
BakkesSizeDF = vis.createDataFrame('size/bakkesmodorgBakkesModSDKSize.csv')
