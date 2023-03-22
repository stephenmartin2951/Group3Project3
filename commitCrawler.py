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


github_token = ["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","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", "insert 3rd token"]
token_counter = 0

while pingsRemaining(github_token[token_counter]) < 100:
        token_counter += 1

api = GhApi(owner=GHOwner, repo=GHRepo, token=github_token[token_counter], ref='heads/master')

def populateCommitData(token_counter, api):  
    pageNum = 1
    while pingsRemaining(github_token[token_counter]) < 100:
        token_counter += 1
        api = GhApi(owner=GHOwner, repo=GHRepo, token=github_token, ref='heads/master')
    commits = api('/repos/{}/{}/commits'.format(GHOwner, GHRepo), 'GET', query=dict(state='all', per_page=100, page=pageNum))
    with open('commits/{}{}Commits.csv'.format(GHOwner,GHRepo), 'w', newline='', encoding="utf-8") as csvfile:
        commitwriter = csv.writer(csvfile)
        commitwriter.writerow(["Author", "Committer", "Commit Date", "Tree URL"])
        #iterate through every issue
        while len(commits) > 0:
            #Write each issue to csv
            for commit in commits:
                commitwriter.writerow([commit.commit.author.name, commit.commit.committer.name, commit.commit.committer.date, commit.commit.tree.url])
            pageNum += 1
            while pingsRemaining(github_token[token_counter]) < 100:
                token_counter += 1
                api = GhApi(owner=GHOwner, repo=GHRepo, token=github_token, ref='heads/master')
            commits = api('/repos/{}/{}/commits'.format(GHOwner, GHRepo), 'GET', query=dict(state='all', per_page=100, page=pageNum))


populateCommitData(token_counter, api)





