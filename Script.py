import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
import streamlit as st


df = pd.read_csv('post_natal.csv')
df = df.drop('Timestamp', axis= 1)
# Lidando com valores ausentes. Excluí as linhas com dados ausentes.
df = df.dropna()


# Renomeando as colunas
df.rename(columns = {'Age': 'Idade', 'Feeling sad or Tearful':'Triste_chorosa',
       'Irritable towards baby & partner':'Irritada', 'Trouble sleeping at night': 'Insonia',
       'Problems concentrating or making decision':'Problema_concentracao',
       'Overeating or loss of appetite': 'Problema_alimentar', 'Feeling anxious': 'Ansiosa', 'Feeling of guilt':'Culpa', 
       'Problems of bonding with baby':'problema_afeto','Suicide attempt':'Tentativa_suicidio'},inplace = True)


# Alterando variável da coluna insonia. Duas ou mais vezes na semana, considerei como sim.

df = df.replace({
    'Problema_concentracao': {'Often': 'Yes'},
    'Insonia': {'Two or more days a week': 'Yes'},
    'Problema_alimentar': {'Not at all': 'No'}
})


# Adicionando titulo do streamlit 
st.title("Dashboard - Saúde Mental Pós-Parto")

# Plotando grafico da faixa etária das maes
counts = df['Idade'].value_counts().sort_index()
fig, ax = plt.subplots()
counts.plot.bar(ax=ax)
ax.set_title('Faixa etária das mães')
for p in ax.patches:
    height = p.get_height()
    ax.annotate(f'{int(height)}',
                xy=(p.get_x() + p.get_width()/2, height),
                xytext=(0, 3),
                textcoords='offset points',
                ha='center', va='bottom',
                fontsize=10, weight='bold')
st.pyplot(fig)

# Gráfico de sintomas mais comuns
st.subheader("Frequência de Sintomas (Geral)")
sintomas = ['Triste_chorosa', 'Irritada', 'Insonia', 'Problema_concentracao',
            'Problema_alimentar', 'Ansiosa', 'Culpa', 'problema_afeto', 'Tentativa_suicidio']
sintomas_counts = {}

for sintoma in sintomas:
    sintomas_counts[sintoma] = df[sintoma].value_counts().get('Yes', 0)

fig3, ax3 = plt.subplots()
ax3.barh(list(sintomas_counts.keys()), list(sintomas_counts.values()))
ax3.set_xlabel("Número de casos")
st.pyplot(fig3)


# criando um filtro por faixa etária
st.subheader("Analisando sentimentos por faixa etária")
df_idade = df['Idade'].unique()
idade_selecionada = st.selectbox("Selecione a faixa etária:", sorted(df_idade))
df_filtrado = df[df['Idade'] == idade_selecionada]

# Avaliando a porcentagem de tentativa de suicídio 
st.subheader("Tentativa de Suicídio")
df_suicide = df_filtrado['Tentativa_suicidio'].value_counts()
cores = ['pink', 'skyblue', 'orange']
fig1, ax1 = plt.subplots()
ax1.pie(df_suicide, labels=df_suicide.index, autopct='%1.1f%%', startangle=90, colors= cores)
ax1.axis('equal')
st.pyplot(fig1)


# Avaliando a proporcao de ansiedade 
st.subheader("Sentimento de ansiedade")
df_ansiedade = df_filtrado['Ansiosa'].value_counts()
fig2, ax2 = plt.subplots()
ax2.bar(df_ansiedade.index, df_ansiedade.values)
ax2.set_xlabel('Resposta')
for p in ax2.patches:
    height = p.get_height()
    ax2.annotate(f'{int(height)}',
                xy=(p.get_x() + p.get_width()/2, height),
                xytext=(0, 3),
                textcoords='offset points',
                ha='center', va='bottom',
                fontsize=10, weight='bold')
st.pyplot(fig2)


# Criacao de um heatmap para correlacionar os sintomar com ansiedade
df = pd.get_dummies(df, columns= ['Insonia', 'Tentativa_suicidio', 'problema_afeto','Problema_concentracao', 'Problema_alimentar', 'Culpa', 'Ansiosa', 'Triste_chorosa', 'Irritada'], dtype='int8')
df_ansiosas = df[df['Ansiosa_Yes'] == 1]
col_sint_yes = [col for col in df.columns if col.endswith('_Yes') and col != 'Ansiosa_Yes']

# Calcular frequência média dos sintomas entre ansiosas

freq_ansiosas = df_ansiosas[col_sint_yes].mean()

heatmap_data = pd.DataFrame(freq_ansiosas).T
st.subheader("Heatmap correlacionando todos os sintomas com ansiedade (dados gerais)")
fig, ax = plt.subplots(figsize=(12, 2))
sns.heatmap(heatmap_data, annot=True, fmt=".1%", cmap="Reds", ax=ax, cbar=False)
ax.set_title("Frequência dos Sintomas entre Ansiosas")
st.pyplot(fig)

import phik
from phik.report import plot_correlation_matrix
phik_matrix = df.phik_matrix()
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(
    phik_matrix,
    cmap="Reds",
    vmin=0, vmax=1,
    annot=False,            # deixe True se quiser números
    square=True,
    cbar_kws={"label": "φk"}
)
ax.set_title("Correlação φk entre sintomas")
st.pyplot(fig)
          






