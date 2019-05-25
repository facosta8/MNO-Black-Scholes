# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import pandas as pd
from datetime import date

external_stylesheets = [
        'C://Users//facosta8//giteando//MNO-Black-Scholes//estilo.css']

app = dash.Dash(__name__)

# TODO: función del tocayo para cargar todo

nombres_comunes = dict({'LBMA/GOLD': 'Gold',
                        'LBMA/SILVER': 'Silver',
                        'CHRIS/CME_PL1': 'Platinum',
                        'CHRIS/CME_O1': 'Oats',
                        'CHRIS/CME_DA1': 'Dairy',
                        'CHRIS/CME_LN1': 'Pork',
                        'CHRIS/CME_C1': 'Corn',
                        'CHRIS/CME_RR1': 'Rice',
                        'CHRIS/CME_LB1': 'Lumber',
                        'CHRIS/CME_RB1': 'Gasoline',
                        'CHRIS/CME_NG1': 'Natural gas',
                        'CHRIS/CME_S1': 'Soybean'
                        })


colors = {
    'background': '#3d3d3d',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']},
                      children=[
    html.H1("Futures Finance Forecast"),


    html.Div(style={'backgroundColor': colors['background']},
             children=[

                daq.NumericInput(id='LBMA/GOLD',
                                 className='numerico',
                                 value=0,
                                 size=100,
                                 min=0,
                                 max=10000,
                                 label='Gold',
                                 style={'color': '#EFEFEF'}),
                html.Br(),

                daq.NumericInput(id='LBMA/SILVER',
                                 className='numerico',
                                 value=0,
                                 size=100,
                                 min=0,
                                 max=10000,
                                 label='Silver'),
                html.Br(),

                daq.NumericInput(id='CHRIS/CME_PL1',
                                 className='numerico',
                                 value=0,
                                 size=100,
                                 min=0,
                                 max=10000,
                                 label='Platinum'),
                html.Br(),      

                daq.NumericInput(id='CHRIS/CME_O1',
                                 className='numerico',
                                 value=0,
                                 size=100,
                                 min=0,
                                 max=10000,
                                 label='Oats'),
                html.Br(),

                daq.NumericInput(id='CHRIS/CME_DA1',
                                 className='numerico',
                                 value=0,
                                 size=100,
                                 min=0,
                                 max=10000,
                                 label='Dairy'),
                html.Br(),

                daq.NumericInput(id='CHRIS/CME_LN1',
                                 className='numerico',
                                 value=0,
                                 size=100,
                                 min=0,
                                 max=10000,
                                 label='Pork'),
                html.Br(),

                daq.NumericInput(id='CHRIS/CME_C1',
                                 className='numerico',
                                 value=0,
                                 size=100,
                                 min=0,
                                 max=10000,
                                 label='Corn'),
                html.Br(),

                daq.NumericInput(id='CHRIS/CME_RR1',
                                 className='numerico',
                                 value=0,
                                 size=100,
                                 min=0,
                                 max=10000,
                                 label='Rice'),
                html.Br(),

                daq.NumericInput(id='CHRIS/CME_LB1',
                                 className='numerico',
                                 value=0,
                                 size=100,
                                 min=0,
                                 max=10000,
                                 label='Lumber'),
                html.Br(),

                daq.NumericInput(id='CHRIS/CME_RB1',
                                 className='numerico',
                                 value=0,
                                 size=100,
                                 min=0,
                                 max=10000,
                                 label='Gasoline'),
                html.Br(),

                daq.NumericInput(id='CHRIS/CME_NG1',
                                 className='numerico',
                                 value=0,
                                 size=100,
                                 min=0,
                                 max=10000,
                                 label='Natural Gas'),
                html.Br(),

                daq.NumericInput(id='CHRIS/CME_S1',
                                 className='numerico',
                                 value=0,
                                 size=100,
                                 min=0,
                                 max=10000,
                                 label='Soybean'),
                html.Br(),

    ], className='listafuturos'),

    html.Div(style={'backgroundColor': colors['background']},
             children=[

                html.Label('Meses a proyectar',
                           className='commodity'),
                daq.Slider(id='meses',
                           min=2,
                           max=24,
                           marks={'2': '2', '6': '6', '12': '12',
                                  '18': '18', '24': '24'},
                           value=24,
                           size=300,
                           handleLabel='meses'
                           ),
                html.Br(),

                html.Button(html.Span('Realizar cálculo'),
                            id='botonCalculo',
                            className='boton2'),
                html.Br(),
                html.Br(),
                html.Br(),

    ], className='areacalculo'),

    html.Div(style={'backgroundColor': colors['background']},
             children=[

                html.P('Run the analysis to see your results',
                       id='textoresultado',
                       className='resultado'),

                html.Img(src=app.get_asset_url('work.gif'),
                         className='puerquito')

    ], className='areacalculo'),

    dcc.Graph(
        id='grafica_valores',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'linear', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'linear', 'name': u'Montréal'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])


#@app.callback(
#    Output('textoresultado', 'children'),
#    [Input('LBMA/GOLD', 'value'),
#     Input('LBMA/SILVER', 'value'),
#     Input('CHRIS/CME_PL1', 'value'),
#     Input('CHRIS/CME_O1', 'value'),
#     Input('CHRIS/CME_DA1', 'value'),
#     Input('CHRIS/CME_LN1', 'value'),
#     Input('CHRIS/CME_C1', 'value'),
#     Input('CHRIS/CME_RR1', 'value'),
#     Input('CHRIS/CME_LB1', 'value'),
#     Input('CHRIS/CME_RB1', 'value'),
#     Input('CHRIS/CME_NG1', 'value'),
#     Input('CHRIS/CME_S1', 'value')
#     ])
#
#def update_texto(in1, in2, in3, in4, in5, in6,
#                 in7, in8, in9, in10, in11, in12):
#
#    todos = dict({'LBMA/GOLD': in1,
#                  'LBMA/SILVER': in2,
#                  'CHRIS/CME_PL1': in3,
#                  'CHRIS/CME_O1': in4,
#                  'CHRIS/CME_DA1': in5,
#                  'CHRIS/CME_LN1': in6,
#                  'CHRIS/CME_C1': in7,
#                  'CHRIS/CME_RR1': in8,
#                  'CHRIS/CME_LB1': in9,
#                  'CHRIS/CME_RB1': in10,
#                  'CHRIS/CME_NG1': in11,
#                  'CHRIS/CME_S1': in12
#                  })
#    validos = dict((k, v) for k, v in todos.items() if v > 0)
#    return 'El cálculo se hizo: {}'.format(len(validos.keys()))


@app.callback(
    Output('grafica_valores', 'figure'),
    [Input('botonCalculo', 'n_clicks')],
    state=[State('LBMA/GOLD', 'value'),
           State('LBMA/SILVER', 'value'),
           State('CHRIS/CME_PL1', 'value'),
           State('CHRIS/CME_O1', 'value'),
           State('CHRIS/CME_DA1', 'value'),
           State('CHRIS/CME_LN1', 'value'),
           State('CHRIS/CME_C1', 'value'),
           State('CHRIS/CME_RR1', 'value'),
           State('CHRIS/CME_LB1', 'value'),
           State('CHRIS/CME_RB1', 'value'),
           State('CHRIS/CME_NG1', 'value'),
           State('CHRIS/CME_S1', 'value'),
           State('meses', 'value')
           ]
    )

def update_graph(n_clicks, in1, in2, in3, in4, in5, in6,
                 in7, in8, in9, in10, in11, in12,
                 meses):
    
    df = pd.read_csv('modelo_simple/datos.csv')
    df.Date = pd.to_datetime(df.Date)

    todos = dict({'LBMA/GOLD': in1,
                  'LBMA/SILVER': in2,
                  'CHRIS/CME_PL1': in3,
                  'CHRIS/CME_O1': in4,
                  'CHRIS/CME_DA1': in5,
                  'CHRIS/CME_LN1': in6,
                  'CHRIS/CME_C1': in7,
                  'CHRIS/CME_RR1': in8,
                  'CHRIS/CME_LB1': in9,
                  'CHRIS/CME_RB1': in10,
                  'CHRIS/CME_NG1': in11,
                  'CHRIS/CME_S1': in12
                  })
    validos = dict((k, v) for k, v in todos.items() if v > 0)
    lista_validos = list(validos.keys())
    cols_seleccionar = lista_validos.copy()
    cols_seleccionar.append('Date')
    df = df[df.Date > (date.today() - pd.offsets.MonthBegin(meses))]
    df = df.filter(items=cols_seleccionar)
    df = df.dropna()
    
    return {
            'data': [ {
                        'x': df.Date,
                        'y': df[commodity],
                        'name': nombres_comunes[commodity],
                        'mode':'lines+markers'
                    } for commodity in lista_validos
                    ],      
            'layout': {
                    'xaxis': {'title': 'Date'},
                    'yaxis': {'title': "Opening value"},
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {'color': colors['text'] }
                      }
        }





if __name__ == '__main__':
    app.run_server(debug=True)