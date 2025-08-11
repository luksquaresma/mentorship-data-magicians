

<h1 align="center"> Saúde Mental no Puerpério — Uma Análise Exploratória de Sintomas em Puérperas </h1>



1. CONTEXTO

A depressão pós‑parto (DPP) é uma condição que afeta cerca de 15 a 20% das mulheres no primeiro ano após o nascimento do bebê. Apesar de ser amplamente estudada, ainda há lacunas na identificação precoce e no entendimento dos fatores de risco que levam uma puérpera a desenvolver sintomas depressivos. O dataset utilizado neste projeto foi extraído do Kaggle e contém respostas de 1503 mulheres que relataram diferentes sentimentos no pós parto. As variáveis são autorrelatos de sintomas (insônia, irritabilidade, ansiedade, problemas de alimentação, dificuldades de afeto com o bebê e ideação suicida) e informações demográficas (idade). Esse dados nao possuem diagnóstico clínico de depressao pós parto, sendo o foco do trabalho uma análise descritiva para entender sintomas e padroes, bem como possíveis grupos de risco para desenvolver DPP. 

2. OBJETIVO

Descrever e entender como os sintomas emocionais no puerpério se distribuem e se sobrepõem entre si, avaliar como e se variam por faixa etária, para identificar perfis de maior vulnerabilidade, sem fazer diagnóstico nem predição.


3. TECNOLOGIAS UTILIZADAS

- Python
- Streamlit
- Pandas
- Matplotlib e Seaborn
- Phik

4. CONTEÚDO DO DATASET

O arquivo 'post_natal.csv' contém 11 colunas com idade (faixa), sintomas, e tentativa de suicídio. 

Entre os isntomas estão: 

- Timestamp (datetime) — data e hora da resposta.

- Age — faixa etária da participante 

- Feeling_sad_or_Tearful 

- Irritable_towards_baby_partner

- Trouble_sleeping_at_night 

- Problems_concentrating_or_making_decision 

- Overeating_or_loss_of_appetite (Yes/No) 

- Feeling_anxious

- Feeling_of_guilt 

- Problems_of_bonding_with_baby

- Suicide_attempt 

5. METODOLOGIA DE ANÁLISE
5.1 Limpeza e preparação:

- Tratamento de valores faltantes

- Renomeação das colunas 

- Substituiçao de variáveis de acordo com seu significado 

- Conversão de respostas Yes/No para valores binários (1/0).

5.2 EDA (Exploratory Data Analysis):

- Estatísticas descritivas e prevalência de cada sintoma.

- Correlação (coeficiente phi) entre sintomas.

- Estratificação por faixa etária.

5.3 Visualizações:

- Gráfico de barras das prevalências de sentimentos.

- Heatmap de correlação entre sintomas.

- Gráficos por faixa etária.

6. PARA EXECUTAR O PROJETO

- Instale as ferramentas do item 3 
- Rode o código
- Em seu terminal digite --> streamlit run Script.py
O navegador abre em http://localhost:8501. Se não abrir, copie o link que aparecer no terminal.

7. REFERENCIAS

Carlson K, Mughal S, Azhar Y, et al. Perinatal Depression. [Updated 2025 Jan 22]. In: StatPearls [Internet]. Treasure Island (FL): StatPearls Publishing; 2025 Jan-. Available from: https://www.ncbi.nlm.nih.gov/books/NBK519070/
Dataset: Kaggle — Postpartum Depression Symptoms ().

