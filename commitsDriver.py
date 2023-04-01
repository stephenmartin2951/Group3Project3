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

PaperMonthCommitDF = utils.frequencyPerDate(PaperCommitsDF, 'Month', 'Number of Commits')
BakkesMonthCommitDF = utils.frequencyPerDate(BakkesCommitsDF, 'Month', 'Number of Commits')
# Visualizes the annual commits over all years of project's lifetime
vis.createLineChart(PaperYearCommitDF, 'Year', 'Number of Commits', 'Commit Year', 'Number of Commits', 'Commits per Year', True, 'PaperCommitsPerYear', 'commitsVis' )
vis.createLineChart(BakkesYearCommitDF, 'Year', 'Number of Commits', 'Commit Year', 'Number of Commits', 'Commits per Year', True, 'BakkesCommitsPerYear', 'commitsVis' )
# Visualizes average commits per month over the project's lifetime
vis.createLineChart(PaperMonthCommitDF, 'Month', 'Number of Commits', 'Month', 'Number of Commits', 'Avg. Commits per Month', True, 'PaperCommitsPerMonth', 'commitsVis' )
vis.createLineChart(BakkesMonthCommitDF, 'Month', 'Number of Commits', 'Month', 'Number of Commits', 'Avg. Commits per Month', True, 'BakkesCommitsPerMonth', 'commitsVis' )
