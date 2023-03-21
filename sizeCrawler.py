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

def populateSizeData():  
    pageNum = 1
    tree = api('/repos/{}/{}/git/trees/HEAD'.format(GHOwner, GHRepo), 'GET', query=dict(recursive=1))
    totalSize = 0
    for branch in tree.tree:
        if hasattr(branch, 'size'):
            totalSize += branch.size
    with open('size/{}{}Size.csv'.format(GHOwner,GHRepo), 'w', newline='', encoding="utf-8") as csvfile:
        commitwriter = csv.writer(csvfile)
        commitwriter.writerow(["Owner", "Repo", "Size"])
        commitwriter.writerow([GHOwner, GHRepo, totalSize])



populateSizeData()