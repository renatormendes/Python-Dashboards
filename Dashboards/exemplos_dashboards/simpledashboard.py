# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""

# meu_dash.py

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# Criando o aplicativo Dash
app = dash.Dash(__name__)

# Carregando dados de exemplo 
# (pode ser substituído pelos seus próprios dados)
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 11, 12, 13, 14],
    'z': [20, 18, 16, 14, 12]
})

# Layout da aplicação
app.layout = html.Div(children=[
    html.H1(children='Aplicação Dash Simples'),
    dcc.Graph(
        id='scatter-plot',
        figure=px.scatter(df, x='x', y='y', size='z', 
                          title='Gráfico de Dispersão')
    )
])

# Executando o servidor
if __name__ == '__main__':
    app.run_server(debug=True)