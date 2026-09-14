# maciel-dissertacao-ros
Implementações e pacotes de replicação da dissertação.

Script em python:
[crawlers/meta_ticket atualizado.py](https://github.com/IntelAgir-Research-Group/maciel-dissertacao-ros/blob/eac103b7e4ff3916c7f33dd5d80f12b98a142267/crawlers/meta_ticket%20atualizado.py)

Planilha com os dados:
[https://docs.google.com/spreadsheets/d/1MyQACe3NBHSMZ0cDebxaglrt1LH8MdxMGVyuz_WDGR4/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1wnRT5tLIqS4raKwnpKlDpS-K4GHbGWf3reEUxIwKiZk/edit?usp=sharing)


# Pacote de Replicação: Um Estudo da Evolução da Segunda Versão do Sistema Operacional para Robótica (ROS 2) com Foco na Eficiência Energética e Manutenibilidade

[![Licença: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![SonarQube](https://img.shields.io/badge/SonarQube-Community%20Edition-brightgreen.svg)](https://www.sonarsource.com/products/sonarqube/)

Este repositório contém o pacote de replicação completo da dissertação de mestrado intitulada **"Um Estudo da Evolução da Segunda Versão do Sistema Operacional para Robótica (ROS 2) com Foco na Eficiência Energética e Manutenibilidade"**, desenvolvida no Programa de Pós-Graduação em Informática (PPGI) da Universidade Tecnológica Federal do Paraná (UTFPR), Campus Cornélio Procópio.

O pacote inclui scripts de extração por Mineração de Repositórios de Software (MSR), planilhas de triagem qualitativa, dados da revisão bibliográfica sistemática, métricas estáticas extraídas via SonarQube e scripts estatísticos não paramétricos para validação de hipóteses.

---

## 📌 Sumário
- [Visão Geral do Estudo](#-visão-geral-do-estudo)
- [Estrutura do Repositório](#-estrutura-do-repositório)
- [Dados da Revisão Bibliográfica (Footnotes da Dissertação)](#-dados-da-revisão-bibliográfica)
- [Conjunto de Dados de Métricas (SonarQube)](#-conjunto-de-dados-de-métricas-sonarqube)
- [Instalação e Pré-requisitos](#-instalação-e-pré-requisitos)
- [Instruções de Execução e Replicação](#-instruções-de-execução-e-replicação)
- [Citação](#-citação)

---

## 🔬 Visão Geral do Estudo

A pesquisa investiga o impacto das decisões arquiteturais introduzidas ao longo de sete distribuições do ROS 2 (*Dashing* a *Jazzy*) no consumo energético e na manutenibilidade do código-fonte. 

* **QP1:** Quais as principais decisões arquiteturais na evolução das distribuições ROS 2 recentes?
* **QP2:** Quais decisões arquiteturais do ROS 2 possuem potencial de impactar a eficiência energética e como elas se categorizam?
* **QP3:** Qual é o impacto da implementação das decisões arquiteturais com potencial energético na manutenibilidade, complexidade e dívida técnica do código-fonte do ROS 2?
* **QP4:** Como se comporta a evolução temporal do volume de código ($\Delta\text{LOC}$) das alterações de escopo energético em comparação às demais alterações no ROS 2?

---

## 📂 Estrutura do Repositório

* `data/`:
  * `systematic_review/`: CSVs com a extração bruta e catalogada dos estudos da literatura (incluindo links e critérios de inclusão/exclusão referenciados nas notas de rodapé da dissertação).
  * `architectural_decisions/`: As 386 decisões arquiteturais extraídas dos meta-tickets e notas de release, as 44 decisões selecionadas com escopo energético e o cálculo de concordância Kappa ($\kappa = 0,54$).
  * `sonarqube_metrics/`: Variações das métricas ($\Delta$) extraídas pelo SonarQube para o grupo selecionado ($N=29$) e grupo não selecionado ($N=109$).
* `scripts/`:
  * `01_mining/`: Scripts em Python para Web Scraping dos meta-tickets e extração de commits (Base SHA e Head SHA).
  * `02_sonarqube_analysis/`: Automação da execução de inspeção estática no SonarQube via modelo SQALE.
  * `03_statistical_analysis/`: Scripts para testes de normalidade (Shapiro-Wilk), testes pareados de Wilcoxon, testes de Mann-Whitney U, Delta de Cliff e geração das séries temporais de burn-up.
* `results/`: Figuras em alta resolução e tabelas estatísticas geradas durante a análise.

---

## 📚 Dados da Revisão Bibliográfica (Footnotes da Dissertação)

Para garantir rastreabilidade direta com o texto da dissertação, os arquivos da revisão sistemática estão organizados em:
* [`data/systematic_review/selected_robotics_arch.csv`](data/systematic_review/selected_robotics_arch.csv): Contém os dados dos artigos mapeados sobre arquitetura em sistemas robóticos (Tabela 2 e Tabela 3 da dissertação).
* [`data/systematic_review/selected_tech_debt_arch.csv`](data/systematic_review/selected_tech_debt_arch.csv): Contém os artigos selecionados sobre débito técnico e cheiros arquiteturais (Tabela 4 e Tabela 5 da dissertação).

> **Nota de Rodapé:** Para referenciar o conjunto completo de artigos e planilhas de triagem na dissertação, utilize o link permanente da pasta `data/systematic_review/`.

---

## 📊 Conjunto de Dados de Métricas (SonarQube)

Os dados de análise estática comparam o estado imediatamente anterior (`Base SHA`) e posterior (`Head SHA`) à mesclagem de cada Pull Request:

* **PRs Selecionados (Escopo Energético - $N=29$):** Arquivo [`data/sonarqube_metrics/selected_prs_metrics.csv`](data/sonarqube_metrics/selected_prs_metrics.csv)
* **PRs Não Selecionados (Grupo de Controle - $N=109$):** Arquivo [`data/sonarqube_metrics/non_selected_prs_metrics.csv`](data/sonarqube_metrics/non_selected_prs_metrics.csv)

Métricas avaliadas:
* $\Delta\text{LOC}$: Variação no volume de linhas de código.
* $\Delta\text{Smells}$: Variação na contagem de Code Smells.
* $\Delta\text{Complexidade}$: Variação na Complexidade Ciclomática de McCabe.
* $\Delta\text{Dívida}$: Variação no esforço de remediação de dívida técnica (em minutos).

---

## 🚀 Instalação e Pré-requisitos

### Requisitos de Ambiente
* Python 3.10 ou superior
* Git instalado e configurado
* Acesso à API do GitHub (recomenda-se configurar um `GITHUB_TOKEN` para evitar limites de taxa)
* SonarQube Server (versão Community Edition testada) e SonarScanner CLI

### Instalação de Dependências
Clone o repositório e configure o ambiente virtual:

```bash
git clone [https://github.com/IntelAgir-Research-Group/](https://github.com/IntelAgir-Research-Group/)<NOME-DO-REPOSITORIO>.git
cd <NOME-DO-REPOSITORIO>

python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt

