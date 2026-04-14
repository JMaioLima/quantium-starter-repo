# Pink Morsel Sales Visualisation Dashboard
# This Dash application visualises sales data for Pink Morsels over time.
# The data was pre-processed in Task 2 to include as fields:
# Sales, Date, and Region.
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# Loading Task 2 processed data
df = pd.read_csv("formatted_data.csv")

# Converting Date column
df["Date"] = pd.to_datetime(df["Date"])

# Grouping and sorting
daily_sales = df.groupby("Date")["Sales"].sum().reset_index()
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

# Layout
app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualisation"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)