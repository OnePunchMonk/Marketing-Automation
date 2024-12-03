import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import streamlit as st

data = pd.read_csv("new_csv.csv")
data["Campaign ID"] = data["Campaign ID"].astype(str)
print(data["Campaign ID"].unique())
campaign_options = [{"label": campaign, "value": campaign} for campaign in data["Campaign ID"].unique()]
print(campaign_options) 

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Campaign Performance Dashboard"),
    html.Div([
        html.Div([
            html.Label("Select Campaign(s):"),

            dcc.Dropdown(
                id="campaign-filter",
                options=[{"label": campaign, "value": campaign} for campaign in data["Campaign ID"].unique()],
                value=data["Campaign ID"].unique(),
                # value=['campaign_1'],
                multi=True
                
            )
             

        ], style={"width": "45%", "display": "inline-block"}),
        

        html.Div([
            html.Label("Select Status:"),
            dcc.Dropdown(
                id="status-filter",
                options=[{"label": status, "value": status} for status in data["Status"].unique()],
                value=data["Status"].unique(),
                multi=True
            )
        ], style={"width": "45%", "display": "inline-block", "margin-left": "10px"})
    ]),

    html.Div(id="filtered-data-table", style={"margin-top": "20px"}),

    html.H2("Click-Through Rate (CTR) by Campaign"),
    dcc.Graph(id="ctr-graph"),

    html.H2("Return on Ad Spend (ROAS) by Campaign"),
    dcc.Graph(id="roas-graph"),

    html.H2("Spend and Revenue Trends"),
    dcc.Graph(id="spend-trends-graph")
])

@app.callback(
    [
        Output("filtered-data-table", "children"),
        Output("ctr-graph", "figure"),
        Output("roas-graph", "figure"),
        Output("spend-trends-graph", "figure")
    ],
    [
        Input("campaign-filter", "value"),
        Input("status-filter", "value")
    ]
)
def update_dashboard(selected_campaigns, selected_status):
    # Filter data
    filtered_data = data[
        (data["Campaign ID"].isin(selected_campaigns)) &
        (data["Status"].isin(selected_status))
    ]

    # Data table
    data_table = html.Div([
        html.H4("Filtered Campaign Data"),
        html.Table([
            html.Thead(html.Tr([html.Th(col) for col in filtered_data.columns])),
            html.Tbody([
                html.Tr([html.Td(row[col]) for col in filtered_data.columns])
                for _, row in filtered_data.iterrows()
            ])
        ], style={"width": "100%", "border": "1px solid black", "border-collapse": "collapse"})
    ])

    # CTR graph
    ctr_fig = px.bar(
        filtered_data,
        x="Campaign ID",
        y="CTR",
        color="Status",
        title="CTR by Campaign",
        labels={"CTR": "Click-Through Rate (%)"},
        color_discrete_map={"Active": "green", "Inactive": "red"}
    )

    # ROAS graph
    roas_fig = px.bar(
        filtered_data,
        x="Campaign ID",
        y="ROAS",
        color="Status",
        title="ROAS by Campaign",
        labels={"ROAS": "Return on Ad Spend"},
        color_discrete_map={"Active": "green", "Inactive": "red"}
    )

    # Spend vs Revenue trends
    spend_fig = px.line(
        filtered_data,
        x="Campaign ID",
        y=["Spend", "Revenue"],
        title="Spend vs Revenue",
        labels={"value": "Amount", "variable": "Metric"},
        markers=True
    )

    return data_table, ctr_fig, roas_fig, spend_fig


if __name__ == "__main__":
    app.run_server(debug=True, port=8051)

st.title("Campaign Performance Dashboard")
st.sidebar.header("Filters")

    # Filters
campaign_filter = st.sidebar.multiselect(
    "Select Campaign(s):",
    options=data["Campaign ID"].unique(),
    default=data["Campaign ID"].unique()
)

status_filter = st.sidebar.multiselect(
    "Select Status:",
    options=data["Status"].unique(),
    default=data["Status"].unique()
)

# Apply filters
filtered_data = data[
    (data["Campaign ID"].isin(campaign_filter)) & 
    (data["Status"].isin(status_filter))
]

# Display filtered data
st.subheader("Filtered Campaign Data")
st.dataframe(filtered_data)

# Visualization: CTR by Campaign
st.subheader("Click-Through Rate (CTR) by Campaign")
ctr_fig = px.bar(
    filtered_data,
    x="Campaign ID",
    y="CTR",
    title="CTR by Campaign",
    labels={"CTR": "Click-Through Rate (%)"},
    color="Status",
    barmode="group",
    color_discrete_map={"Active": "green", "Inactive": "red"}
)
st.plotly_chart(ctr_fig)

# Visualization: ROAS by Campaign
st.subheader("Return on Ad Spend (ROAS) by Campaign")
roas_fig = px.bar(
    filtered_data,
    x="Campaign ID",
    y="ROAS",
    title="ROAS by Campaign",
    labels={"ROAS": "Return on Ad Spend"},
    color="Status",
    barmode="group",
    color_discrete_map={"Active": "green", "Inactive": "red"}
)
st.plotly_chart(roas_fig)


st.subheader("Spend and Revenue Trends")
spend_fig = px.line(
    filtered_data,
    x="Campaign ID",
    y=["Spend", "Revenue"],
    title="Spend vs Revenue",
    labels={"value": "Amount", "variable": "Metric"},
    markers=True
)
st.plotly_chart(spend_fig)

st.write("Use the filters in the sidebar to refine the data shown in the graphs.")

