from ghapi.all import GhApi
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--owner", type=str)
parser.add_argument("-r", "--repo", type=str)
args=parser.parse_args()
GHOwner = args.owner
GHRepo = args.repo

if(GHOwner == None):
    GHOwner = 'PaperMC'

if(GHRepo == None):
    GHRepo = 'Paper'


github_token = "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"

api = GhApi(owner=GHOwner, repo=GHRepo, token=github_token, ref='heads/master')

def populateCommitData():  
    return
    ####################################
    #TODO: Refactor for commits
    ####################################
    # pageNum = 1
    # issues = api('/repos/{}/{}/issues'.format(GHOwner, GHRepo), 'GET', query=dict(state='all', per_page=100, page=pageNum))
    # with open('{}Commits.csv'.format(GHRepo), 'w', newline='') as csvfile:
    #     issuewriter = csv.writer(csvfile)
    #     issuewriter.writerow(["State", "Labels", "Assignees", "Comments", "Closed_At", "Created_At", "Locked"])
    #     #iterate through every issue
    #     while(len(issues) > 0):
    #         #Write each issue to csv
    #         for issue in issues:
    #             issuewriter.writerow([issue.state, issue.labels, len(issue.assignees), issue.comments, issue.closed_at, issue.created_at, issue.locked])
    #         pageNum += 1
    #         issues = api('/repos/{}/{}/issues'.format(GHOwner, GHRepo), 'GET', query=dict(state='all', per_page=100, page=pageNum))  


populateCommitData()





