# Pink Morsel Sales Visualisation Dashboard
# This Dash application visualises sales data for Pink Morsels over time.
# The data was pre-processed in Task 2 to include as fields:
# Sales, Date, and Region.

from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# Loading Task 2 processed data
df = pd.read_csv("formatted_data.csv")

# Converting Date column
df["Date"] = pd.to_datetime(df["Date"])

# Grouping and sorting
# daily_sales = df.groupby("Date")["Sales"].sum().reset_index()
# daily_sales = daily_sales.sort_values("Date")

app.layout = html.Div([

    html.H1(
        "Pink Morsel Sales Visualisation",
        style={
            "textAlign": "center",
            "marginBottom": "30px"
        }
    ),

    html.P(
        "Explore sales trends by region",
        style={
            "textAlign": "center",
            "marginBottom": "20px"
        }
    ),

    # Radio buttons for region filtering
    dcc.RadioItems(
        id="region-filter",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "South", "value": "south"},
            {"label": "East", "value": "east"},
            {"label": "West", "value": "west"},
        ],
        value="all",
        labelStyle={
            "display": "inline-block",
            "marginRight": "25px",
            "color": "#55495E",
            "fontWeight": "bold"
        },
        style={
            "display": "flex",
            "justifyContent": "center",
            "textAlign": "center",
            "marginBottom": "30px"
        },
        inputStyle={"marginRight": "6px"}
    ),

    dcc.Graph(id="sales-chart")

], className="container")

# Callback to update graph based on selected region
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)

def update_graph(selected_region):

    # Filter dataset
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"] == selected_region]

    # Group and sort
    daily_sales = filtered_df.groupby("Date")["Sales"].sum().reset_index()
    daily_sales = daily_sales.sort_values("Date")

    # Creating the line chart
    fig = px.line(
        daily_sales,
        x="Date",
        y="Sales",
        title="Pink Morsel Sales Over Time",
        labels={
            "Date": "Date",
            "Sales": "Total Sales"
        }
    )

    # Adding styling to the chart
    fig.update_layout(
        title_font_size=24,
        title_font_color="#55495E",
        xaxis_title_font_size=18,
        yaxis_title_font_size=18,
        plot_bgcolor="#F0F0F0",
        paper_bgcolor="#F9F9F9",
        font_color="#55495E"
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)