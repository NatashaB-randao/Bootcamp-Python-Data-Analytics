# Descrição do Desafio - Módulo 3: Processamento de Dados Simplificado com Power BI

Olá, pessoal! Neste documento, irei descrever o projeto realizado no módulo 3, focado no processamento de dados simplificado utilizando o Power BI. Ao longo deste projeto, enfrentamos desafios relacionados à integração de dados, transformação e modelagem no Power BI, utilizando uma base de dados disponível no GitHub e uma instância MySQL na plataforma Azure.

## 1. Criação de uma Instância na Azure para MySQL
Inicialmente, configuramos uma instância no Microsoft Azure para hospedar nosso banco de dados MySQL. Isso nos permitiu armazenar e gerenciar os dados de forma segura e escalável.

## 2. Criação do Banco de Dados com Base Disponível no GitHub
Utilizamos uma base de dados disponível no GitHub como ponto de partida para nosso projeto. Importamos esses dados para nossa instância MySQL na Azure, preparando o ambiente para a integração com o Power BI.

## 3. Integração do Power BI com MySQL no Azure
Configuramos a conexão entre o Power BI e o banco de dados MySQL hospedado na Azure. Isso nos permitiu acessar e manipular os dados diretamente no Power BI para análise e visualização.

## 4. Verificação de Problemas na Base para Realização da Transformação dos Dados
Identificamos problemas na base de dados que precisavam ser corrigidos antes da análise. Esses problemas incluíam valores nulos, tipos de dados inconsistentes e colunas complexas.

## 5. Diretrizes para Transformação dos Dados
Definimos diretrizes para a transformação dos dados, incluindo:

- Verificação dos cabeçalhos e tipos de dados.
- Conversão dos valores monetários para o tipo double preciso.
- Análise e tratamento de valores nulos.
- Identificação e preenchimento de lacunas nos dados, como colaboradores sem gerentes ou departamentos sem gerentes.
- Verificação do número de horas dos projetos.
- Separação e simplificação de colunas complexas.
- Mescla de consultas para criar tabelas agregadas e otimizadas para análise.

## 6. Mescla de Dados para Criar Tabelas Agregadas e Otimizadas
Realizamos a mescla de dados para criar tabelas agregadas, como a associação de colaboradores aos seus respectivos departamentos e gerentes. Isso foi feito utilizando consultas SQL ou mesclando tabelas diretamente no Power BI.

## 7. Agrupamento de Dados e Eliminação de Colunas Desnecessárias
Agrupamos os dados para determinar quantos colaboradores existem por gerente. Além disso, eliminamos colunas desnecessárias que não seriam utilizadas nos relatórios finais, simplificando assim as tabelas e otimizando o desempenho do modelo.

## 8. Explicação sobre Utilização de Mesclar em Vez de Atribuir
No processo de mescla de dados, optamos por utilizar o recurso de mesclar em vez de atribuir, pois a mescla nos permitiu combinar e agregar os dados de forma flexível, facilitando a análise e visualização posterior. A atribuição de dados teria limitado nossa capacidade de manipulação e agregação dos dados.

Este projeto nos proporcionou uma experiência prática valiosa em processamento de dados utilizando o Power BI, preparando-nos para desafios mais complexos no futuro.