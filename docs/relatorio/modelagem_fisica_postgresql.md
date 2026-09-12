# Modelagem Física PostgreSQL - FinanceWeb

## Objetivo

Definir a estrutura física do banco de dados da aplicação FinanceWeb utilizando PostgreSQL.

A modelagem física foi construída a partir da modelagem conceitual previamente definida, contemplando as entidades usuários, receitas, despesas e metas financeiras.

---

# Tabela: usuarios

```sql
CREATE TABLE usuarios (

    id SERIAL PRIMARY KEY,

    nome VARCHAR(100) NOT NULL,

    email VARCHAR(150) NOT NULL UNIQUE,

    telefone_whatsapp VARCHAR(20),

    senha VARCHAR(255) NOT NULL,

    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    ativo BOOLEAN DEFAULT TRUE

);
```

---

# Tabela: receitas

```sql
CREATE TABLE receitas (

    id SERIAL PRIMARY KEY,

    usuario_id INTEGER NOT NULL,

    descricao VARCHAR(255) NOT NULL,

    categoria VARCHAR(100),

    valor DECIMAL(10,2) NOT NULL,

    data_recebimento DATE NOT NULL,

    recorrente BOOLEAN DEFAULT FALSE,

    observacao TEXT,

    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (usuario_id)
        REFERENCES usuarios(id)

);
```

---

# Tabela: despesas

```sql
CREATE TABLE despesas (

    id SERIAL PRIMARY KEY,

    usuario_id INTEGER NOT NULL,

    descricao VARCHAR(255) NOT NULL,

    categoria VARCHAR(100),

    valor DECIMAL(10,2) NOT NULL,

    data_lancamento DATE NOT NULL,

    data_vencimento DATE,

    data_pagamento DATE,

    status VARCHAR(20) DEFAULT 'Pendente',

    observacao TEXT,

    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (usuario_id)
        REFERENCES usuarios(id)

);
```

---

# Tabela: metas

```sql
CREATE TABLE metas (

    id SERIAL PRIMARY KEY,

    usuario_id INTEGER NOT NULL,

    titulo VARCHAR(150) NOT NULL,

    descricao TEXT,

    valor_meta DECIMAL(10,2) NOT NULL,

    valor_atual DECIMAL(10,2) DEFAULT 0,

    data_inicio DATE,

    data_limite DATE,

    status VARCHAR(20) DEFAULT 'Em andamento',

    FOREIGN KEY (usuario_id)
        REFERENCES usuarios(id)

);
```

---

# Relacionamentos

## Usuários e Receitas

```text
usuarios (1) → (N) receitas
```

---

## Usuários e Despesas

```text
usuarios (1) → (N) despesas
```

---

## Usuários e Metas

```text
usuarios (1) → (N) metas
```

---

# Status Utilizados

## Despesas

```text
Pendente
Paga
Atrasada
Cancelada
```

## Metas

```text
Em andamento
Concluída
Cancelada
```

---

# Considerações Técnicas

## Chaves Primárias

Todas as tabelas utilizam:

```sql
SERIAL PRIMARY KEY
```

permitindo geração automática de identificadores únicos.

---

## Integridade Referencial

As tabelas:

- receitas
- despesas
- metas

possuem chave estrangeira:

```sql
usuario_id
```

garantindo vínculo obrigatório com a tabela usuarios.

---

## Controle Temporal

O sistema registra automaticamente:

```sql
CURRENT_TIMESTAMP
```

para controle de criação dos registros.

---

## Controle Financeiro de Despesas

A entidade despesas contempla:

- Data de lançamento;
- Data de vencimento;
- Data de pagamento;
- Status.

Essa estrutura permite diferenciar despesas registradas, pendentes, vencidas e efetivamente pagas, fornecendo suporte adequado para dashboards financeiros e acompanhamento de obrigações futuras.

---

# Versão

Modelagem Física v1.0

Data: 12/09/2026

Projeto Integrador em Computação II

FinanceWeb
``