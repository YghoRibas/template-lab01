import requests
from datetime import datetime

token = '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'

url = 'https://api.github.com/graphql'


def run_query(cursor=None):
  query = """
    query ($cursor: String) {
      search(query: "stars:>1", type: REPOSITORY, first: 100, after: $cursor) {
        edges {
          node {
            ... on Repository {
              name
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
              updatedAt
              createdAt
            }
          }
        }
        pageInfo {
          endCursor
          hasNextPage
        }
      }
    }
    """

  headers = {
      'Authorization': f'Bearer {token}',
  }

  response = requests.post(url,
                           json={
                               'query': query,
                               'variables': {
                                   'cursor': cursor
                               }
                           },
                           headers=headers)

  if response.status_code == 200:
    data = response.json()
    repositories = data['data']['search']['edges']
    page_info = data['data']['search']['pageInfo']
    return repositories, page_info['endCursor'] if page_info[
        'hasNextPage'] else None
  else:
    print(f'Erro na requisição: {response.status_code}, {response.text}')
    return None, None


all_repositories = []
cursor = None

for i in range(10):
  repositories, cursor = run_query(cursor)
  if not repositories:
    break
  all_repositories.extend(repositories)

with open('resultados.txt', 'w') as file:
  file.write(
      f'Nome, Idade, PRs, ultima atualização, razão de issues, linguagem principal\n'
  )
  for repo in all_repositories:
    name = repo['node']['name']
    created_at = repo['node']['createdAt']
    updated_at = repo['node']['updatedAt']
    PRs = repo['node']['pullRequests']['totalCount']
    primary_language = repo['node']['primaryLanguage']['name'] if repo['node'][
        'primaryLanguage'] else None

    closed_issues = repo['node']['issuesClosed']['totalCount']
    total_issues = repo['node']['issues']['totalCount']

    issue_relationship = closed_issues / total_issues if total_issues > 0 else 0

    created_date = datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%SZ')
    current_date = datetime.now()

    updated_date = datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%SZ')
    updated_date_formatted = updated_date.strftime('%d/%m/%Y')

    age_years = (current_date - created_date).days / 365

    result_line = f' {name}, {age_years:.0f},  {PRs}, {updated_date_formatted}, {issue_relationship: .2f}, {primary_language}\n'
    file.write(result_line)

print("Resultados salvos")
