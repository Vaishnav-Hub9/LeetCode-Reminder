import requests
import json
from datetime import datetime, timezone

def fetch_recent_submissions(username: str, limit: int = 1) -> list:
    """
    Fetches the recent accepted submissions for a given LeetCode username.
    Returns a list of submission dictionaries.
    """
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
        "limit": limit
    }
    payload = {
        "query": query,
        "variables": variables
    }
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Extract the submissions
        if "data" in data and "recentAcSubmissionList" in data["data"]:
            return data["data"]["recentAcSubmissionList"]
        else:
            print(f"Failed to find submissions data for {username}: {data}")
            return []
    except Exception as e:
        print(f"Error fetching data for {username}: {e}")
        return []

def has_submitted_today(username: str) -> bool:
    """
    Checks if the user has made any accepted submissions today (strictly calculated in UTC).
    """
    submissions = fetch_recent_submissions(username, limit=1)
    
    if not submissions:
        return False
        
    latest_submission = submissions[0]
    timestamp_str = latest_submission.get("timestamp")
    
    if not timestamp_str:
        return False
        
    # LeetCode timestamps are stringified Unix timestamps in seconds
    submission_time_utc = datetime.fromtimestamp(int(timestamp_str), tz=timezone.utc)
    
    # Get current time in UTC
    current_time_utc = datetime.now(timezone.utc)
    
    # Compare just the date part (year, month, day)
    if submission_time_utc.date() == current_time_utc.date():
        return True
        
    return False

if __name__ == "__main__":
    # Small test
    test_user = "neal_wu"
    print(f"Testing for {test_user}...")
    submissions = fetch_recent_submissions(test_user)
    print(f"Latest submission data: {submissions}")
    print(f"Has {test_user} submitted today (UTC)? {has_submitted_today(test_user)}")
