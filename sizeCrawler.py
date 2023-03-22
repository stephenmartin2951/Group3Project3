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

def getCommitTrees(token_counter):
    pageNum = 1
    while pingsRemaining(github_token[token_counter]) < 100:
        token_counter += 1
    api = GhApi(owner=GHOwner, repo=GHRepo, token=github_token[token_counter], ref='heads/master')        
    commits = api('/repos/{}/{}/commits'.format(GHOwner, GHRepo), 'GET', query=dict(state='all', per_page=100, page=pageNum))
    shas = []
    dates = []
    while len(commits) > 0:
        for commit in commits:
            shas.append(commit.commit.tree.sha)
            dates.append(commit.commit.committer.date)
        pageNum += 1
        while pingsRemaining(github_token[token_counter]) < 100:
            token_counter += 1
        commits = api('/repos/{}/{}/commits'.format(GHOwner, GHRepo), 'GET', query=dict(state='all', per_page=100, page=pageNum))

    return shas, dates    

def populateSizeData(token_counter):  
    shas, dates = getCommitTrees(token_counter)
    sizeArr = []
    for sha in shas:
        while pingsRemaining(github_token[token_counter]) < 100:
            token_counter += 1
            api = GhApi(owner=GHOwner, repo=GHRepo, token=github_token[token_counter], ref='heads/master')    
        tree = api('/repos/{}/{}/git/trees/{}'.format(GHOwner, GHRepo, sha), 'GET', query=dict(recursive=1))
        totalSize = 0
        for branch in tree.tree:
            if hasattr(branch, 'size'):
                totalSize += branch.size
        sizeArr.append(totalSize)
    with open('size/{}{}Size.csv'.format(GHOwner,GHRepo), 'w', newline='', encoding="utf-8") as csvfile:
        commitwriter = csv.writer(csvfile)
        commitwriter.writerow(["Owner", "Repo", "Size", "Date"])
        for size, date in zip(sizeArr, dates):
            commitwriter.writerow([GHOwner, GHRepo, size, date])            


populateSizeData(token_counter)