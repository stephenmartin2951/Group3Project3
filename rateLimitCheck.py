from ghapi.all import GhApi

def pingsRemaining(github_token):  
    api = GhApi(token=github_token)
    remaining =  api('/rate_limit', 'GET')
    return remaining.resources.core.remaining
