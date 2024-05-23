import requests
from config import API_URL, ACCESS_TOKEN

def get_posts(team_id, channel_id):
    url = f"{API_URL}/teams/{team_id}/channels/{channel_id}/posts"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    return response.json()
