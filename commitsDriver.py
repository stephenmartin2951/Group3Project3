import visualizations as vis
import utils
#Create Commit DataFrames
PaperCommitsDF = vis.createDataFrame('commits/PaperMCPaperCommits.csv')
BakkesCommitsDF = vis.createDataFrame('commits/bakkesmodorgBakkesModSDKCommits.csv')

PaperCommitsDF = utils.addYear(PaperCommitsDF, 'Commit Date', 'Year')
PaperCommitsDF = utils.addMonth(PaperCommitsDF, 'Commit Date', 'Month')
BakkesCommitsDF = utils.addYear(BakkesCommitsDF, 'Commit Date', 'Year')
BakkesCommitsDF = utils.addMonth(BakkesCommitsDF, 'Commit Date', 'Month')

PaperYearCommitDF = utils.frequencyPerDate(PaperCommitsDF, 'Year', 'Number of Commits')
BakkesYearCommitDF = utils.frequencyPerDate(BakkesCommitsDF, 'Year', 'Number of Commits')


vis.createLineChart(PaperYearCommitDF, 'Year', 'Number of Commits', 'Commit Year', 'Number of Commits', 'Commits per Year', True, 'PaperCommitsPerYear', 'commitsVis' )
vis.createLineChart(BakkesYearCommitDF, 'Year', 'Number of Commits', 'Commit Year', 'Number of Commits', 'Commits per Year', True, 'BakkesCommitsPerYear', 'commitsVis' )
