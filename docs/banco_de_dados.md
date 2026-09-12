# Modelagem do Banco de Dados - FinanceWeb

## Tabela: usuarios

| Campo | Tipo | Descrição |
|---------|---------|---------|
| id | INTEGER | Identificador único do usuário |
| nome | VARCHAR(100) | Nome completo |
| email | VARCHAR(150) | E-mail do usuário |
| telefone_whatsapp | VARCHAR(20) | Número do WhatsApp |
| senha | VARCHAR(255) | Senha criptografada |
| data_cadastro | TIMESTAMP | Data e hora do cadastro |
| ativo | BOOLEAN | Situação da conta |

---

## Tabela: receitas

| Campo | Tipo | Descrição |
|---------|---------|---------|
| id | INTEGER | Identificador da receita |
| usuario_id | INTEGER | Usuário proprietário da receita |
| descricao | VARCHAR(255) | Descrição da receita |
| categoria | VARCHAR(100) | Categoria da receita |
| valor | DECIMAL(10,2) | Valor recebido |
| data_recebimento | DATE | Data do recebimento |
| recorrente | BOOLEAN | Indica se a receita é recorrente |
| observacao | TEXT | Observações adicionais |
| criado_em | TIMESTAMP | Data e hora do registro |

---

## Tabela: despesas

| Campo | Tipo | Descrição |
|---------|---------|---------|
| id | INTEGER | Identificador da despesa |
| usuario_id | INTEGER | Usuário proprietário da despesa |
| descricao | VARCHAR(255) | Descrição da despesa |
| categoria | VARCHAR(100) | Categoria da despesa |
| valor | DECIMAL(10,2) | Valor da despesa |
| data_lancamento | DATE | Data em que a despesa foi lançada no sistema |
| data_vencimento | DATE | Data prevista para pagamento |
| data_pagamento | DATE | Data em que a despesa foi efetivamente paga |
| status | VARCHAR(20) | Situação da despesa |
| observacao | TEXT | Observações adicionais |
| criado_em | TIMESTAMP | Data e hora do registro |

---

## Tabela: metas

| Campo | Tipo | Descrição |
|---------|---------|---------|
| id | INTEGER | Identificador da meta |
| usuario_id | INTEGER | Usuário proprietário da meta |
| titulo | VARCHAR(150) | Nome da meta financeira |
| descricao | TEXT | Descrição detalhada da meta |
| valor_meta | DECIMAL(10,2) | Valor objetivo da meta |
| valor_atual | DECIMAL(10,2) | Valor acumulado até o momento |
| data_inicio | DATE | Data inicial da meta |
| data_limite | DATE | Prazo para conclusão |
| status | VARCHAR(20) | Situação da meta |

---

## Relacionamentos

usuarios (1) → (N) receitas

usuarios (1) → (N) despesas

usuarios (1) → (N) metas

---

## Categorias Sugeridas

### Receitas

- Salário
- 13° Salário
- PLR
- Freelance
- Comissão
- Investimentos
- Aluguel Recebido
- Presentes
- Outros

### Despesas

- Moradia
- Alimentação
- Transporte
- Saúde
- Educação
- Lazer
- Investimentos
- Assinaturas
- Impostos
- Outros

### Status das Despesas

- Pendente
- Paga
- Atrasada
- Cancelada

### Status das Metas

- Em andamento
- Concluída
- Cancelada