import pandas as pd
import dash
from dash import html, dcc
import plotly.express as px
import os

# === 資料讀取 ===
csv_path = os.path.join("dataset", "US_stock_data.csv")
df = pd.read_csv(csv_path)

# === 簡單視覺化 ===
fig = px.line(df, x="date", y="close", color="symbol", title="Stock Prices Over Time")

# === Dash App ===
app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("📈 US Stock Dashboard"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    app.run_server(host="0.0.0.0", port=port)
