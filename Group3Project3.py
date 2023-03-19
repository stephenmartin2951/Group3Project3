from ghapi.all import GhApi
import csv

github_token = "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"

api = GhApi(owner='PaperMC', repo='Paper', token=github_token, ref='heads/master')

def populateIssueData():  
    pageNum = 1
    issues = api('/repos/PaperMC/Paper/issues', 'GET', query=dict(state='all', per_page=100, page=pageNum))
    #iterate through every issue
    with open('paperIssues.csv', 'w', newline='') as csvfile:
        issuewriter = csv.writer(csvfile)
        issuewriter.writerow(["State", "Labels", "Assignees", "Comments", "Closed_At", "Created_At", "Locked"])
        while(len(issues) > 0):
            #Write each issue to csv
            for issue in issues:
                issuewriter.writerow([issue.state, issue.labels, len(issue.assignees), issue.comments, issue.closed_at, issue.created_at, issue.locked])
            pageNum += 1
            issues = api('/repos/PaperMC/Paper/issues', 'GET', query=dict(state='all', per_page=100, page=pageNum))  


populateIssueData()

#TODO: We can now populate data. We can import CSV into whichever tool we use to create visualization





