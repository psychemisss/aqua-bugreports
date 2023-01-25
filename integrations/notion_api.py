import requests
import json
from helpers.config_manager import load_env_variable


class NotionAPI:
    def __init__(self):
        self.database = load_env_variable('NOTION_DATABASE')
        self.secret = load_env_variable('NOTION_SECRET')
        self.version = load_env_variable('NOTION_VERSION')

        self.headers = {
            "Authorization": f"Bearer {self.secret}",
            "Content-Type": "application/json",
            "Notion-Version": self.version
        }

        self.urls = {
            "database": f"https://api.notion.com/v1/databases/{self.database}",
            "pages": "https://api.notion.com/v1/pages"
        }

        self.ping()

    def ping(self) -> None:
        result = requests.request("GET", self.urls['database'], headers=self.headers)

        if result.status_code != 200:
            print(result.text)
            raise Exception("Notion API is not available")
        else:
            print("Notion API is available")

    def create_report(self, name: str = "Undefined", description: str = "Undefined", attachments: str = "Undefined") -> None:

        page_data = {
            "parent": {
                "database_id": self.database
            },
            "icon": {
                "type": "emoji",
                "emoji": "🚫"
            },
            "properties": {
                "Name": {
                    "title": [
                        {
                            "text": {
                                "content": name
                            },
                        }
                    ],
                },
                "Priority": {
                    "select": {
                        "name": "High"
                    }
                },
                "Tags": {
                    "multi_select": [
                        {
                            "name": "Bug"
                        }
                    ]
                }
            },
            "children": [
                {
                    "object": "block",
                    "type": "heading_2",
                    "heading_2": {
                        "rich_text": [{"type": "text", "text": {"content": "Шаги воспроизведения"}}]
                    }
                },
                {
                    "paragraph": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": description
                                }
                            }
                        ]
                    }
                },
                {
                    "paragraph": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                        "content": attachments,
                                }
                            }
                        ]
                    }
                },
            ]
        }

        data = json.dumps(page_data)
        result = requests.request("POST", self.urls['pages'], headers=self.headers, data=data)

        if result.status_code != 200:
            print(result.text)
            raise Exception("Report storing failed")
        else:
            print("Report stored to Notion")
