# Comp470Group3Project3
 Creating a tool to mine software repositories

paperIssues.csv is where issue data pulled using ghapi is stored

issuesCrawler.py uses GhApi to pull issues data and write it to CSV. Args = -o --owner for Repo owner and -r --repo for repo name. 

DigestableIssuesExample.txt has a nicely formatted look at what type of data is pulled through the API.

TODO: Pull down commit data

TODO: Create visualizations using CSV data. Preferably in Python. Thinking we can use a combination of Pandas + Matplotlib

