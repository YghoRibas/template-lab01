import requests
from datetime import datetime

token = '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'

url = 'https://api.github.com/graphql'

query = """
{
  search(query: "stars:>1", type: REPOSITORY, first: 100) {
    edges {
      node {
        ... on Repository {
          name
          createdAt
          updatedAt
          pullRequests(states: MERGED) {
            totalCount
          }
          primaryLanguage {
            name
          }
          issues {
            totalCount
          }
          issuesClosed: issues(states: CLOSED) {
            totalCount
          }
        }
      }
    }
  }
}
"""

headers = {
    'Authorization': f'Bearer {token}',
}

response = requests.post(url, json={'query': query}, headers=headers)

if response.status_code == 200:
  data = response.json()

  print(f'Relatório:')
  repositories = data['data']['search']['edges']
  for repo in repositories:
    name = repo['node']['name']
    created_at = repo['node']['createdAt']
    PRs = repo['node']['pullRequests']['totalCount']
    updated_at = repo['node']['updatedAt']
    primary_language = repo['node']['primaryLanguage']['name'] if repo['node']['primaryLanguage'] else 'null'

    closed_issues = repo['node']['issuesClosed']['totalCount']
    total_issues = repo['node']['issues']['totalCount']

    issues_relationship = closed_issues / total_issues if total_issues > 0 else 0

    current_date = datetime.now()
    
    created_date = datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%SZ')
    age = (current_date - created_date).days/365

    updated_date = datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%SZ')
    updated_date_formatted = updated_date.strftime('%d/%m/%Y')

    print(f'{name}, {age:.0f}, {PRs}, {updated_date_formatted}, {primary_language}, {issues_relationship:.2f}')

else:
  print(f'Erro na requisição: {response.status_code}, {response.text} ')
