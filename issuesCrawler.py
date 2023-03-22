from ghapi.all import GhApi
import csv
import argparse
from rateLimitCheck import pingsRemaining

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


github_token = ["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","insert 2nd token", "insert 3rd token"]
token_counter = 0

while pingsRemaining(github_token[token_counter]) < 100:
        token_counter += 1

api = GhApi(owner=GHOwner, repo=GHRepo, token=github_token[token_counter], ref='heads/master')

def populateIssueData(token_counter, api):  
    pageNum = 1
    while pingsRemaining(github_token[token_counter]) < 100:
        token_counter += 1
        api = GhApi(owner=GHOwner, repo=GHRepo, token=github_token[token_counter], ref='heads/master')
    issues = api('/repos/{}/{}/issues'.format(GHOwner, GHRepo), 'GET', query=dict(state='all', per_page=100, page=pageNum))
    with open('issues/{}{}Issues.csv'.format(GHOwner,GHRepo), 'w', newline='', encoding="utf-8") as csvfile:
        issuewriter = csv.writer(csvfile)
        issuewriter.writerow(["State", "Labels", "Assignees", "Comments", "Closed_At", "Created_At", "Locked"])
        #iterate through every issue
        while(len(issues) > 0):
            #Write each issue to csv
            for issue in issues:
                issuewriter.writerow([issue.state, issue.labels, len(issue.assignees), issue.comments, issue.closed_at, issue.created_at, issue.locked])
            pageNum += 1
            while pingsRemaining(github_token[token_counter]) < 100:
                token_counter += 1
                api = GhApi(owner=GHOwner, repo=GHRepo, token=github_token[token_counter], ref='heads/master')
            issues = api('/repos/{}/{}/issues'.format(GHOwner, GHRepo), 'GET', query=dict(state='all', per_page=100, page=pageNum))  


populateIssueData(token_counter, api)





