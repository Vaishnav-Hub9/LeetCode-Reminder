import requests
import json

def get_recent_submissions(username):
    url = "https://leetcode.com/graphql"
    query = """
    query recentAcSubmissions($username: String!, $limit: Int!) {
        recentAcSubmissionList(username: $username, limit: $limit) {
            id
            title
            titleSlug
            timestamp
        }
    }
    """
    variables = {
        "username": username,
        "limit": 1
    }
    payload = {
        "query": query,
        "variables": variables
    }
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    print(response.status_code)
    print(response.text)

if __name__ == "__main__":
    get_recent_submissions("neal_wu") # using a known active user
