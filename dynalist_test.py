import config

import requests

def add_to_dynalist_inbox(content, token):
    
    url = 'https://dynalist.io/api/v1/inbox/add'
    headers = {'Content-Type': 'application/json'}
    data = {
        'token': token,
        'content': content
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()

if __name__ == "__main__":
    
    dynalist_key = config.DYNLIST_API_KEY
    
    INBOX_CONTENT = 'your_inbox_item_content_here'
    result = add_to_dynalist_inbox(INBOX_CONTENT, dynalist_key)