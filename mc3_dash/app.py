import dash
from dash import dcc, html, Input, Output, ctx
import dash_bootstrap_components as dbc
import pandas as pd
import geopandas as gpd
import plotly.express as px
import plotly.graph_objects as go
import json
from shapely import wkt

# Load data
mc3 = pd.read_csv("mc3_updated.csv")
mc3["geometry"] = mc3["geometry"].apply(lambda x: wkt.loads(x) if pd.notnull(x) else None)
mc3 = gpd.GeoDataFrame(mc3, geometry="geometry", crs="EPSG:4269")
mc3 = mc3.to_crs(epsg=4326)
geojson_data = json.loads(mc3.to_json())

# Define color scale and demographic options
color_scale = [
    "#f8f9fa", "#e3f2f4", "#c6e1e4", "#99ccd2", "#66b7bf", 
    "#3aa3ad", "#1a8a97", "#11727f", "#0a5a68"
]

# Demographic columns
demographic_cols = [
    'Total Population',
    'Population Density (per km2)',
    'Median Income (Dollars)',
    'Percent of Non-White',
    'Rate of OBGYNs (per 100,000 population)',
    'Total # of OBGYNs',
    'Total Consultations'
]

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
app.title = "MC3 Dashboard"

app.layout = dbc.Container([
    html.H2("MC3 Dashboard", className="text-primary text-center fs-3"),

    # Metric Cards
    dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H5("Total Population", className="card-title"),
            html.H3(f"{int(mc3['Total Population'].sum()):,}", className="card-text")
        ])), width=4),
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H5("Total OBGYNs", className="card-title"),
            html.H3(f"{int(mc3['Total # of OBGYNs'].sum()):,}", className="card-text")
        ])), width=4),
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H5("Median Income (Avg)", className="card-title"),
            html.H3(f"${int(mc3['Median Income (Dollars)'].mean()):,}", className="card-text")
        ])), width=4)
    ], className="mb-4"),

    # Main content (map and selection elements)
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='map-graph', style={'height': '600px'}, config={'displayModeBar': False})

        ], md=8),
        dbc.Col([
            html.Label("Select a Demographic to Visualize", className="fw-bold"),
            dcc.Dropdown(
                id='demographic-dropdown',
                options=[{'label': col, 'value': col} for col in demographic_cols],
                value='Rate of OBGYNs (per 100,000 population)'
            ),
            html.Label("Click on the map OR select a county below to view more details", className="fw-bold mt-3"),
            dcc.Dropdown(
                id='single-county-dropdown',
                options=[{'label': name, 'value': name} for name in sorted(mc3['Name'].dropna())],
                value=None,
                placeholder="Select a county"
            ),
            html.Button("Reset", id="reset-btn", className="btn btn-outline-secondary btn-sm my-2"),
            html.Div([
                html.H5(id='selected-county', className="text-info fw-bold mt-3"),
                html.Div(id='sidebar-county-details')
            ])
        ], md=4)
    ], className="mb-4"),

    # Comparison and download row
    dbc.Row([
        dbc.Col([
            html.Label("Compare Multiple Counties", className="fw-bold"),
            dcc.Dropdown(
                id='multi-county-dropdown',
                options=[{'label': name, 'value': name} for name in sorted(mc3['Name'].dropna())],
                multi=True,
                placeholder="Select counties to compare"
            ),
            #html.Button("Download Selected", id="download-button", className="btn btn-outline-primary btn-sm my-2"),
            #dcc.Download(id="download-data"),
            dcc.Graph(id='multi-demographics-chart'),
            html.P("Note: These values are raw counts or rates per county. No adjustments for population have been made.", className="text-muted mt-2"),
            html.P("Counties with a Rate of OBGYNs under 5 per 100K may indicate areas with limited provider access.", className="text-muted")
        ])
    ])
], fluid=True)

@app.callback(
    Output('map-graph', 'figure'),
    Input('demographic-dropdown', 'value')
)
def update_map(selected_demo):
    fig = px.choropleth(
        mc3,
        geojson=geojson_data,
        locations='Name',
        featureidkey="properties.Name",
        color=selected_demo,
        color_continuous_scale=color_scale,
        hover_name='Name',
        hover_data={'Total Consultations': True, selected_demo: True},
        scope="usa",
        labels={selected_demo: selected_demo}
    )
    fig.update_geos(fitbounds="locations", visible=False, projection_scale=6)
    fig.update_layout(
        margin={"r":0, "t":0, "l":0, "b":0},
        coloraxis_colorbar=dict(
            title=selected_demo.replace("(", "<br>("),
            tickfont=dict(size=10),
            titlefont=dict(size=11),
            len=0.4, y=0.5
        )
    )
    return fig

@app.callback(
    Output('selected-county', 'children'),
    Output('sidebar-county-details', 'children'),
    Output('single-county-dropdown', 'value'),
    Output('multi-demographics-chart', 'figure'),
    Input('map-graph', 'clickData'),
    Input('demographic-dropdown', 'value'),
    Input('multi-county-dropdown', 'value'),
    Input('single-county-dropdown', 'value'),
    Input('reset-btn', 'n_clicks'),
    prevent_initial_call=True
)
def update_county_info(clickData, selected_demo, multi_selected, dropdown_selection, reset_clicks):
    triggered = ctx.triggered_id

    if triggered == 'reset-btn':
        return "NONE", "", None, go.Figure()
    elif triggered == 'map-graph' and clickData:
        county_name = clickData['points'][0]['location']
    elif triggered == 'single-county-dropdown' and dropdown_selection:
        county_name = dropdown_selection
    else:
        county_name = None

    if county_name:
        county_data = mc3[mc3['Name'] == county_name].iloc[0]
        county_title = county_name.upper()
        details = html.Div([
            html.P(f"Total Consultations: {int(county_data['Total Consultations']):,}"),
            html.P(f"Rate of OBGYNs: {county_data['Rate of OBGYNs (per 100,000 population)']:.2f} per 100K"),
            html.P(f"Median Income: ${int(county_data['Median Income (Dollars)']):,}"),
            html.P(f"Percent Non-White: {county_data['Percent of Non-White']:.1f}%"),
            html.P(f"Population Density: {county_data['Population Density (per km2)']:.1f}/km²")
        ])
    else:
        county_title = "NONE"
        details = "Click a county on the map or select one from dropdown."

    if multi_selected and len(multi_selected) >= 2:
        comparison_df = mc3[mc3['Name'].isin(multi_selected)]
        fig2 = px.bar(
            comparison_df,
            x='Name',
            y=selected_demo,
            title=f"Selected Counties - {selected_demo}",
            labels={selected_demo: selected_demo},
            color_discrete_sequence=['#1a8a97'] * len(comparison_df)
        )
    else:
        fig2 = go.Figure()

    return county_title, details, county_name, fig2

if __name__ == '__main__':
    app.run(debug=True)
