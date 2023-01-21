import requests
import json


def read_database(databaseId: str = NOTION_DATABASE, headers: dict = NOTION_HEADERS):
    url = f"https://api.notion.com/v1/databases/{databaseId}/query"

    res = requests.request("POST", url, headers=headers)
    data = res.json()
    print(res.status_code)
    # print(res.text)

    with open('./db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)


read_database()
