# Comp470Group3Project3
 Creating a tool to mine software repositories

paperIssues.csv is where issue data pulled using ghapi is stored

issuesCrawler.py uses GhApi to pull issues data and write it to CSV. Args = -o --owner for Repo owner and -r --repo for repo name. 

DigestableIssuesExample.txt has a nicely formatted look at what type of issues data is pulled through the API.

commitsCrawler.py uses GhAPI to pull commit data from all of a given repo's commits and write it to a CSV. Args same as issuesCrawler.py (see above).

TODO: Create visualizations using CSV data. Preferably in Python. Thinking we can use a combination of Pandas + Matplotlib

TODO: Use our scripts/visualizations to analyze additional repositories
