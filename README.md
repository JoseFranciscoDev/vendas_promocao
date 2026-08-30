# Automação de Relatório de Vendas em Promoção

Automação criada para eliminar o processo manual de geração do relatório de vendas
de produtos em promoção, que antes exigia buscar códigos de produto em uma planilha
e colar manualmente em uma query SQL todo mês.

## Tecnologias

- Python
- Pandas
- mysql-connector-python

## Como funciona

### 1. Extração dos códigos de produto da planilha

Os códigos dos produtos em promoção mudam todo mês e ficam em uma planilha do
Google Sheets. O script busca essa planilha exportando-a como CSV diretamente
pela URL, sem precisar de autenticação via API:

```python
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"
df = (
    pd.read_csv(url, skiprows=3, header=0)
    .dropna(how="all")["COD PROD."]
    .dropna()
    .astype(int)
)
```

### 2. Montagem dinâmica da query SQL

A query original era executada manualmente, colando os códigos de produto em um
`IN (...)`. O script monta essa cláusula dinamicamente a partir dos códigos
extraídos da planilha e a insere na query completa.

### 3. Execução no banco de dados

A query final é executada via `mysql-connector`, usando um usuário com permissão
somente leitura, para reduzir o risco de qualquer operação indevida no banco.

## Segurança

- Acesso ao banco feito exclusivamente com usuário read-only.
