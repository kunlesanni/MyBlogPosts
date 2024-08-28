import requests
import json
import os
import markdown

f = open('testmd.md', 'r')
htmlmarkdown=markdown.markdown( f.read() )

url = "https://dev.to/api/articles"

payload = json.dumps({
  "article": {
    "title": "Test Article3",
    "body_markdown": htmlmarkdown,
    "published": False,
    "series": "IaC Articles",
    "main_image": "https://github.com/kunlesanni/MyBlogPosts/blob/main/2024/June/TerraformStateWithTFC/images/tfdod.JPG?raw=true",
    "description": "Small talk about IaC best practices",
    "tags": ["test", "python", "devto"],
    "organization_id": 0
  }
})

api_key = os.getenv('DEVTO_TOKEN')

headers = {
  'api-key': api_key,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
