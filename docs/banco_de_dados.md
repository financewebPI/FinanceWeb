# Modelagem do Banco de Dados - FinanceWeb

## Tabela: usuarios

| Campo | Tipo | Descrição |
|---------|---------|---------|
| id | INTEGER | Identificador |
| nome | VARCHAR(100) | Nome completo |
| email | VARCHAR(150) | E-mail |
| telefone_whatsapp | VARCHAR(20) | Número do WhatsApp |
| senha | VARCHAR(255) | Senha criptografada |
| data_cadastro | TIMESTAMP | Data do cadastro |
| ativo | BOOLEAN | Situação da conta |

---

## Tabela: receitas

| Campo | Tipo | Descrição |
|---------|---------|---------|
| id | INTEGER | Identificador |
| usuario_id | INTEGER | Usuário |
| descricao | VARCHAR(255) | Descrição da receita |
| valor | DECIMAL(10,2) | Valor |
| data | DATE | Data |

---

## Tabela: despesas

| Campo | Tipo | Descrição |
|---------|---------|---------|
| id | INTEGER | Identificador |
| usuario_id | INTEGER | Usuário |
| descricao | VARCHAR(255) | Descrição |
| categoria | VARCHAR(100) | Categoria |
| valor | DECIMAL(10,2) | Valor |
| data | DATE | Data |

---

## Tabela: metas

| Campo | Tipo | Descrição |
|---------|---------|---------|
| id | INTEGER | Identificador |
| usuario_id | INTEGER | Usuário |
| descricao | VARCHAR(255) | Meta |
| valor_meta | DECIMAL(10,2) | Objetivo financeiro |
| valor_atual | DECIMAL(10,2) | Valor acumulado |

---

## Relacionamentos

usuarios (1) → (N) receitas

usuarios (1) → (N) despesas

usuarios (1) → (N) metas