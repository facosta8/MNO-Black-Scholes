# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
from dash.dependencies import Input, Output

external_stylesheets = [
        'C://Users//facosta8//giteando//MNO-Black-Scholes//estilo.css']

app = dash.Dash(__name__)



colors = {
    'background': '#3d3d3d',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']},
                      children=[
    html.H1("Futures Finance Forecast"),


    html.Div(style={'backgroundColor': colors['background']},
             children=[

                html.Label('Gold    ',
                           className='commodity',
                           style={'display': 'inline'}),
                dcc.Input(id='LBMA/GOLD',
                          placeholder=0,
                          value='number',
                          type='number',
                          inputMode='numeric',
                          style={'display': 'inline'}),
                html.Br(),

                html.Label('Silver    ',
                           className='commodity',
                           style={'display': 'inline'}),
                dcc.Input(id='LBMA/SILVER',
                          placeholder=0,
                          value='number',
                          type='number',
                          inputMode='numeric',
                          style={'display': 'inline'}),
                html.Br(),

                html.Label('Platinum    ',
                           className='commodity',
                           style={'display': 'inline'}),
                dcc.Input(id='CHRIS/CME_PL1',
                          placeholder=0,
                          value='number',
                          type='number',
                          inputMode='numeric',
                          style={'display': 'inline'}),
                html.Br(),

                html.Label('Oats      ',
                           className='commodity',
                           style={'display': 'inline'}),
                dcc.Input(id='CHRIS/CME_O1',
                          placeholder=0,
                          value='number',
                          type='number',
                          inputMode='numeric',
                          style={'display': 'inline'}),
                html.Br(),

                html.Label('Dairy    ',
                           className='commodity',
                           style={'display': 'inline'}),
                dcc.Input(id='CHRIS/CME_DA1',
                          placeholder=0,
                          value='number',
                          type='number',
                          inputMode='numeric',
                          style={'display': 'inline'}),
                html.Br(),

                html.Label('Pork         ',
                           className='commodity',
                           style={'display': 'inline'}),
                dcc.Input(id='CHRIS/CME_LN1',
                          placeholder=0,
                          value='number',
                          type='number',
                          inputMode='numeric',
                          style={'display': 'inline'}),
                html.Br(),

                html.Label('Corn    ',
                           className='commodity',
                           style={'display': 'inline'}),
                dcc.Input(id='CHRIS/CME_C1',
                          placeholder=0,
                          value='number',
                          type='number',
                          inputMode='numeric',
                          style={'display': 'inline'}),
                html.Br(),

                html.Label('Rice    ',
                           className='commodity',
                           style={'display': 'inline'}),
                dcc.Input(id='CHRIS/CME_RR1',
                          placeholder=0,
                          value='number',
                          type='number',
                          inputMode='numeric',
                          style={'display': 'inline'}),
                html.Br(),

                html.Label('Lumber    ',
                           className='commodity',
                           style={'display': 'inline'}),
                dcc.Input(id='CHRIS/CME_LB1',
                          placeholder=0,
                          value='number',
                          type='number',
                          inputMode='numeric',
                          style={'display': 'inline'}),
                html.Br(),

                html.Label('Gasoline    ',
                           className='commodity',
                           style={'display': 'inline'}),
                dcc.Input(id='CHRIS/CME_RB1',
                          placeholder=0,
                          value='number',
                          type='number',
                          inputMode='numeric',
                          style={'display': 'inline'}),
                html.Br(),

                html.Label('Natural Gas    ',
                           className='commodity',
                           style={'display': 'inline'}),
                dcc.Input(id='CHRIS/CME_NG1',
                          placeholder=0,
                          value='number',
                          type='number',
                          inputMode='numeric',
                          style={'display': 'inline'}),
                html.Br(),

                html.Label('Soybean    ',
                           className='commodity',
                           style={'display': 'inline'}),
                dcc.Input(id='CHRIS/CME_S1',
                          placeholder=0,
                          value='number',
                          type='number',
                          inputMode='numeric',
                          style={'display': 'inline'}),
                html.Br(),

    ], className='listafuturos'),

    html.Div(style={'backgroundColor': colors['background']},
             children=[

                html.Label('Ajuste',
                           className='commodity'),
                daq.Slider(id='ssss',
                           min=50,
                           max=100,
                           marks={'50': '50', '60': '60', '70': '70',
                                  '80': '80', '90': '90', '100': '100'},
                           value=70,
                           size=300,
                           handleLabel='r^2',
                           step=10
                           ),
                html.Br(),

                html.Label('Meses a proyectar',
                           className='commodity'),
                daq.Slider(id='dasda',
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
        id='example-graph-2',
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


@app.callback(
    Output(component_id='textoresultado', component_property='children'),
    [Input(component_id='CL', component_property='value')]
)
def update_output_div(input_value):
    return 'El valor estimado de tu portafolio es {}'.format(input_value)


if __name__ == '__main__':
    app.run_server(debug=True)
