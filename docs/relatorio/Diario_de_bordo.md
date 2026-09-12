# Diário de Bordo - FinanceWeb

## Projeto Integrador em Computação II

### Projeto
FinanceWeb

### Objetivo Geral

Desenvolver uma aplicação web denominada FinanceWeb para gerenciamento de finanças pessoais, permitindo o controle de receitas, despesas, metas financeiras e indicadores de desempenho financeiro, utilizando tecnologias web modernas, banco de dados relacional, APIs externas, computação em nuvem e controle de versão.

---

# Integrantes

- Áurea De Souza Ângelo
- Edson Cesar Biajante Leme
- Gerson Vieira Dos Santos Junior
- Jessé Benício
- Thiago Ortiz De Oliveira
- Vinícius Costa Damaceno de Araújo

---

# Registro das Atividades

## Data: 07/09/2026

---

### Atividade 01 - Definição do Projeto

#### Objetivo

Definir o tema do Projeto Integrador e a solução que será desenvolvida.

#### Descrição

Após análise dos requisitos da disciplina, foi definido o desenvolvimento de uma aplicação web denominada FinanceWeb, voltada ao gerenciamento de finanças pessoais.

O sistema terá como objetivo auxiliar usuários no controle de receitas, despesas, metas financeiras e acompanhamento da situação financeira por meio de dashboards e relatórios.

#### Resultado

Tema definido para desenvolvimento.

---

### Atividade 02 - Criação da Conta Google do Projeto

#### Objetivo

Criar uma identidade digital exclusiva para o projeto.

#### Descrição

Foi criada uma conta Google exclusiva para o FinanceWeb, destinada ao gerenciamento dos serviços e plataformas utilizados durante o desenvolvimento.

A conta será utilizada para integração com GitHub, Render e demais serviços necessários.

#### Resultado

Conta criada com sucesso.

---

### Atividade 03 - Criação da Conta GitHub

#### Objetivo

Implementar o controle de versão do projeto.

#### Descrição

Foi criada uma conta GitHub específica para o projeto FinanceWeb.

A plataforma será utilizada para armazenamento do código-fonte, controle de versões, colaboração entre os integrantes e acompanhamento da evolução do desenvolvimento.

#### Resultado

Ambiente de versionamento criado.

---

### Atividade 04 - Criação da Conta Render

#### Objetivo

Preparar o ambiente de hospedagem em nuvem.

#### Descrição

Foi criada uma conta na plataforma Render e realizada sua integração inicial com o GitHub.

O serviço será utilizado futuramente para realizar o deploy da aplicação FinanceWeb em ambiente de produção.

#### Resultado

Infraestrutura de hospedagem preparada.

---

### Atividade 05 - Criação do Repositório FinanceWeb

#### Objetivo

Centralizar os arquivos e o código-fonte do projeto.

#### Descrição

Foi criado o repositório oficial do projeto FinanceWeb no GitHub.

Configurações iniciais:

- Repositório público;
- Arquivo README.md;
- Arquivo .gitignore para Python;
- Licença MIT.

#### Resultado

Repositório criado e configurado.

---

### Atividade 06 - Definição da Arquitetura Tecnológica

#### Objetivo

Selecionar as tecnologias que serão utilizadas durante o desenvolvimento.

#### Tecnologias Definidas

| Tecnologia | Finalidade            |
|------------|-----------------------|
| Flask      | Backend               |
| HTML       | Estrutura das páginas |
| CSS        | Estilização           |
| Bootstrap  | Responsividade        |
| JavaScript | Interatividade        |
| PostgreSQL | Banco de dados        |
| GitHub     | Versionamento         |
| Render     | Hospedagem            |
| Chart.js   | Gráficos              |
| AwesomeAPI | Consulta de cotações  |

#### Resultado

Arquitetura tecnológica aprovada.

---

### Atividade 07 - Levantamento Inicial de Requisitos

#### Objetivo

Identificar as funcionalidades do sistema.

#### Requisitos Funcionais

- Cadastro de usuários;
- Login;
- Cadastro de receitas;
- Cadastro de despesas;
- Dashboard financeiro;
- Metas financeiras;
- Consulta de cotação monetária através de API.

#### Requisitos Não Funcionais

- Interface responsiva;
- Acessibilidade;
- Segurança dos dados;
- Hospedagem em nuvem;
- Controle de versão através do GitHub.

#### Resultado

Primeira versão dos requisitos elaborada.

---

### Atividade 08 - Estruturação da Documentação do Projeto

#### Objetivo

Organizar a documentação técnica.

#### Descrição

Foi criada a pasta "docs" dentro do repositório do projeto.

Também foram criados os arquivos:

- README.md;
- requisitos.md.

A documentação será mantida junto ao código-fonte para facilitar o controle de versões.

#### Commit Realizado

docs: criação da estrutura de documentação

#### Resultado

Estrutura inicial da documentação criada.

---

### Atividade 09 - Clonagem do Repositório para Ambiente Local

#### Objetivo

Preparar o ambiente de desenvolvimento local.

#### Descrição

O repositório FinanceWeb foi clonado da plataforma GitHub para a máquina de desenvolvimento.

Foi utilizado Git integrado ao Visual Studio Code.

#### Resultado

Projeto disponível para desenvolvimento local.

---

### Atividade 10 - Configuração do Ambiente de Desenvolvimento

#### Objetivo

Definir a ferramenta principal de desenvolvimento.

#### Descrição

Foi configurado o ambiente de desenvolvimento utilizando:

- Visual Studio Code;
- Git;
- GitHub;
- Python;
- Terminal PowerShell.

#### Resultado

Ambiente preparado para desenvolvimento da aplicação.

---

### Atividade 11 - Criação da Estrutura Inicial da Aplicação

#### Objetivo

Preparar a estrutura básica do sistema.

##### Estrutura Criada

```text
FinanceWeb
│
├── app
│   ├── static
│   │   ├── css
│   │   ├── img
│   │   └── js
│   └── templates
│
├── docs
│
├── tests
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

##### Resultado

Estrutura inicial da aplicação criada e preparada para o desenvolvimento das funcionalidades do sistema.

### Atividade 12 - Implementação Inicial do Flask

#### Objetivo

Criar a base do backend da aplicação.

#### Descrição

Foi criado o arquivo principal da aplicação denominado "app.py".
Também foi criado o arquivo "requirements.txt" com a dependência inicial do framework Flask.

#### Commit Realizado

feat: estrutura inicial Flask

#### Resultado
Estrutura inicial do backend criada.

### Atividade 13 - Problema de Permissão no GitHub

#### Objetivo

Realizar o primeiro envio de alterações para o repositório remoto.

#### Problema Encontrado

Ao executar o comando:
 
git push origin main

foi apresentada uma falha de permissão.

#### Diagnóstico

Foi identificado que o usuário pessoal utilizado no computador não possuía permissão para realizar alterações no repositório FinanceWeb.

#### Solução Aplicada

O usuário pessoal foi adicionado como colaborador do projeto.

#### Resultado
Problema resolvido.

### Atividade 14 - Configuração do Trabalho Colaborativo

#### Objetivo

Permitir rastreabilidade das contribuições individuais.

#### Descrição

Foi adotada a seguinte estratégia:

- Conta FinanceWeb como proprietária do projeto;
- Conta pessoal JBen21 como colaborador.

Dessa forma, todas as contribuições ficam registradas individualmente no histórico do GitHub.

#### Resultado

Ambiente colaborativo configurado.

### Atividade 15 - Primeiro Fluxo Completo de Versionamento

#### Objetivo

Validar o processo de desenvolvimento baseado em Git.

#### Descrição

##### Foram executadas com sucesso as etapas:

git add .

git commit

git push

Com isso foi validada a integração entre:
Ambiente local;
GitHub;
Controle de versão.

#### Resultado

Fluxo de versionamento funcionando corretamente.

### Atividade 16 - Restauração da Documentação

#### Objetivo

Garantir a integridade dos documentos do projeto.

#### Descrição

Durante a organização inicial da estrutura do projeto, o arquivo README.md da pasta de documentação foi removido acidentalmente.
O arquivo foi recriado e sincronizado novamente com o repositório.

##### Commit Realizado

docs: restaura README da documentação

#### Resultado

Documentação restaurada com sucesso.

### Atividade 17 - Evolução dos Requisitos de Usuário

#### Objetivo

Preparar a estrutura do sistema para futuras integrações com serviços de autenticação e comunicação.

#### Descrição

Foi adicionada à modelagem da tabela de usuários a informação de telefone WhatsApp. A inclusão foi planejada para permitir futuramente a implementação de recuperação de senha por token, autenticação em duas etapas e envio de notificações relacionadas às funcionalidades do sistema FinanceWeb.

#### Resultado

Modelagem preparada para futuras integrações com APIs de mensageria.

### Atividade 18 - Primeira Execução Local da Aplicação

#### Objetivo

Validar a configuração do ambiente de desenvolvimento e a estrutura inicial da aplicação.

#### Descrição

Foi realizada a primeira execução local da aplicação FinanceWeb utilizando o framework Flask.

A aplicação foi iniciada através do arquivo principal app.py e disponibilizada localmente por meio do servidor de desenvolvimento do Flask.

O acesso foi realizado através do endereço:

http://127.0.0.1:5000

#### Resultado

Aplicação executada com sucesso em ambiente local, validando a estrutura inicial do backend e a configuração do ambiente de desenvolvimento.

### Atividade 19 - Definição da Identidade Visual

#### Objetivo

Definir os padrões visuais do sistema FinanceWeb.

#### Descrição

Foi criada a documentação de identidade visual do projeto, incluindo logotipo, paleta de cores, tipografia, slogan e diretrizes de interface.

As cores escolhidas foram inspiradas em soluções modernas do setor financeiro, priorizando confiança, tecnologia e experiência do usuário.

#### Resultado

Identidade visual definida para utilização nas próximas etapas de desenvolvimento.

### Atividade 20 - Desenvolvimento da Landing Page

#### Objetivo

Criar a primeira interface visual do sistema FinanceWeb.

#### Descrição

Foi desenvolvida a primeira versão da Landing Page do sistema utilizando HTML e CSS.

A página passou a utilizar a identidade visual oficial do projeto, incluindo logotipo, paleta de cores institucional, botões personalizados e área de apresentação das principais funcionalidades do sistema.

Também foram implementados ajustes de layout utilizando CSS Grid para melhorar a organização e responsividade dos componentes.

#### Resultado

Primeira interface visual do FinanceWeb concluída e disponível em ambiente local.

#### Atividade 21 - Refinamento da Landing Page

##### Objetivo

Melhorar a experiência visual e a organização dos componentes da página inicial do sistema.

##### Descrição

Foram realizados ajustes na Landing Page do FinanceWeb visando melhorar o contraste visual, a hierarquia dos elementos e a responsividade da interface.

A seção de funcionalidades foi reestruturada utilizando CSS Grid, permitindo o alinhamento uniforme dos cards e melhor adaptação para diferentes tamanhos de tela.

Também foram realizados ajustes em espaçamentos, sombras e organização visual dos componentes.

##### Resultado

Landing Page refinada com melhor organização visual, maior conforto de leitura e estrutura preparada para evolução das próximas funcionalidades.

## Data: 10/09/2026

#### Atividade 22 - Implementação da Navbar

##### Objetivo:

Criar uma estrutura de navegação reutilizável para o sistema.

##### Descrição:

Foi implementada a primeira versão da navbar do FinanceWeb utilizando a identidade visual definida para o projeto.

Também foram realizados ajustes na organização dos arquivos CSS, removendo estilos duplicados e centralizando a estilização dos botões em componentes reutilizáveis.

##### Resultado:

Navbar funcional implementada e arquitetura CSS refinada para suportar o crescimento do sistema.

## Data: 11/09/2026

#### Atividade 23 - Implementação da Tela de Login

##### Objetivo

Criar uma estrutura de login

##### Descrição:

Foi criada a primeira versão da tela de Login do FinanceWeb utilizando componentes reutilizáveis de interface, incluindo formulário de autenticação, navegação para 

recuperação de senha e acesso ao cadastro de novos usuários.

Também foram desenvolvidos componentes reutilizáveis para formulários, incluindo campos de entrada de dados, agrupamento de campos e cartão visual de autenticação, que 

poderão ser reutilizados em telas futuras como Cadastro e Recuperação de Senha.

##### Resultado:
Sistema passou a possuir fluxo inicial de autenticação e navegação entre Landing Page, Login e Cadastro.

## Situação Atual do Projeto

### Concluído

✅ Definição do projeto
✅ Criação das contas de serviço
✅ GitHub configurado
✅ Render configurado
✅ Estrutura do repositório criada
✅ Arquitetura tecnológica definida
✅ Levantamento inicial de requisitos
✅ Documentação inicial criada
✅ Ambiente local configurado
✅ Estrutura Flask criada
✅ Controle de versão funcionando
✅ Colaboradores configurados
✅ Definir o fluxo das telas do sistema
✅ Criar documentação das telas
✅ Executar aplicação Flask localmente
✅ Criar primeira interface HTML
✅ Landing Page
✅ Navbar
✅ Tela de Login

### Próximas Atividades

🔄 Implementar Tela de Cadastro
🔄 Modelar banco de dados
🔄 Integrar PostgreSQL
🔄 Implementar Recuperação de Senha
🔄 Implementar Dashboard Financeiro
🔄 Integrar AwesomeAPI
🔄 Realizar deploy no Render

# Considerações Finais

O projeto FinanceWeb encontra-se na fase inicial de desenvolvimento. Até o momento foram concluídas as etapas de planejamento, configuração de ambiente, preparação da infraestrutura em nuvem, definição tecnológica, estruturação da documentação e implementação da base inicial da aplicação.

As próximas atividades serão focadas na modelagem das telas, banco de dados, implementação das funcionalidades e publicação da aplicação.
