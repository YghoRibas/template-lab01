# Relatório

## Sprint 1 
Query utilizada com paginação

    query {
      search(query: "stars:>1", type: REPOSITORY, first: 100) {
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
      }
    }


Resultados recolhidos salvos em  [resultadosq1.txt](https://github.com/YghoRibas/template-lab01/blob/bb57bc9f22950686bd14b09cef82f02e0dc0e566/scripts/dataset/resultadosq1.txt) 
## Sprint 2 

Query utilizada com paginação

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

Resultados recolhidos salvos em  [resultadosq2.txt](https://github.com/YghoRibas/template-lab01/blob/bb57bc9f22950686bd14b09cef82f02e0dc0e566/scripts/dataset/resultadosq2.txt) 

# Hipótese
Para essa pesquisa foram utilizados os 1000 repositórios que possuem mais estrelas.

### Hipótese informal para os RQs:
Minha hipótese para esse laboratório, é de que os repositórios são antigos (mais que 5 anos desde sua criação), são atualizados frequentemente e que possuem uma relação de resolução de issues significativas (maior que 0.75). O Sucesso desses repositórios não dependem da linguagem utilizada e sim da ideia proposta e sua solução para resolver determinado problema.

