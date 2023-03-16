from dash import Dash, html, dcc
import pandas as pd
import numpy as np
from scipy.integrate import odeint
import plotly.express as px
from dash.dependencies import Input, Output

app = Dash(__name__, title='Página Bruno Trindade')

server = app.server


#####################


t = np.linspace(0, 50, 1000)

texto = 'No instante $t=0$, um tanque contém $Q_0$ kg de sal dissolvidos em $100 l$ de água. ' \
        'Suponha que água contendo $\\frac{1}{4}$ kg de sal por litro está entrando no tanque' \
        ' a uma taxa de $r$ litros por minuto e que o líquido, bem misturado, está saindo' \
        ' do tanque à mesma taxa. Seja $Q(t)$ a quantidade de sal no tempo $t$ e suponha ' \
        ' que o sal não é criado nem destruído no tanque. Logo, temos a seguinte equação ' \
        ' diferencial para a taxa de variação de sal no tanque:'

formula = '$\\displaystyle  \\frac{dQ}{dt}= \\frac{r}{4} - \\frac{rQ}{100}$'

app.layout = html.Div([html.Div([html.H1('MATEMÁTICA APLICADA', style={'text-align': 'center'}), html.Div([html.P(dcc.Markdown('### Exemplo:', mathjax=True), style={'margin': '20px'}), html.P(dcc.Markdown(texto, mathjax=True), style={'margin': '20px'}), html.P(dcc.Markdown(formula, mathjax=True), style={'margin': '20px', 'padding-bottom': '20px'})])]), html.Div([html.Div([html.H3('Digite o valor de r:'), dcc.Input(id='r', value=8.69, type='number')], style={'background-color': '#add8e6', 'width': '200px', 'height': '100px',
                      'border-radius': '20px', 'text-align': 'center', 'padding': '10px', 'border': '2px solid bisque'}), html.Div([html.H3(dcc.Markdown('Digite o valor de $Q_0:$', mathjax=True)), dcc.Input(id='entrada', value=30, type='number')], style={'background-color': '#add8e6', 'width': '200px', 'height': '100px', 'border-radius': '20px', 'text-align': 'center', 'padding': '10px', 'border': '2px solid bisque'})], style={'display': 'flex', 'textAlign': 'center', 'margin-left': '10px'}), dcc.Graph(id='fig', mathjax=True)])


@app.callback(
    Output(component_id='fig', component_property='figure'),
    Input(component_id='r', component_property='value'),
    Input(component_id='entrada', component_property='value')
)
def g(r, y0):
    if (r == None) or (y0 == None):
        fig = px.line()
        return fig
    else:
        def f(y, t):
            f = r / 4 - r * y / 100
            return f
        sol = odeint(f, y0, t)
        df = pd.DataFrame()
        df['tempo'] = pd.DataFrame(t)
        df['Q(t)'] = pd.DataFrame(sol)
        fig = px.line(df, x=df['tempo'], y=df['Q(t)'], title='Solução Gráfica')
        return fig


if __name__ == '__main__':
    app.run_server(debug=True)
