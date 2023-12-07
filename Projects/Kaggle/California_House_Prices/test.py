import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Carregar os dados
url = 'https://raw.githubusercontent.com/rvanguita/DataScientists/main/Projects/Kaggle/California_House_Prices/data/housing.csv'
df = pd.read_csv(url)

# Preparar os dados
df_filtered = df[['median_house_value', 'ocean_proximity', 'median_income']]
df_filtered = df_filtered[df_filtered['ocean_proximity'] == '<1H OCEAN']

# Criar o Dash app
app = dash.Dash(__name__)

# Layout do Dash app
app.layout = html.Div([
    html.H1("Casas Mais Caras em Comparação com a Distância da Praia"),
    dcc.Graph(id='scatter-plot')
])

# Callback para atualizar o gráfico com as casas mais caras em relação à distância da praia
@app.callback(
    dash.dependencies.Output('scatter-plot', 'figure'),
    [dash.dependencies.Input('scatter-plot', 'value')]
)
def update_graph():
    fig = px.scatter(df_filtered, x='median_income', y='median_house_value', 
                     hover_name='ocean_proximity', title='Casas Mais Caras vs. Distância da Praia',
                     labels={'median_income': 'Renda Média', 'median_house_value': 'Valor Mediano das Casas'})
    return fig

# Rodar o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
