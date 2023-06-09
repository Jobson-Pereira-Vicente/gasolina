#Exercício - Módulo **18**
#Nome: Jobson Pereira Vicente


%%writefile gasolina.csv


import pandas as pd
gasolina_df = pd.read_csv('gasolina.csv', sep=',')


gasolina_df


import seaborn as sns


grafico = sns.lineplot(data=gasolina_df, x="dia", y="venda", ci=None, color="red")

for i in grafico.patches:
  grafico.annotate(i.get_height(),
                (i.get_x() +i.get_width() /1, i.get_height()),
                ha='center')

grafico.set(title='Preço Médio da Gasolina na Cidade de Sâo Paulo', xlabel='Dia - 07/2021', ylabel='Valor Médio')

grafico.get_figure().savefig('projeto/gasolina.png')