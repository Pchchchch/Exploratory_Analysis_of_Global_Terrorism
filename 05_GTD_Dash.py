#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# 데이터 로드
df = pd.read_parquet("data/interim/gtd_clean.parquet")

# 집계
df_year_region = (
    df.groupby(["iyear", "region_txt"])
      .size()
      .reset_index(name="attacks")
)

app = Dash(__name__)

app.layout = html.Div([
    html.H2("Global Terrorism Trends Dashboard"),

    dcc.Dropdown(
        id="region-dropdown",
        options=[
            {"label": r, "value": r}
            for r in sorted(df_year_region["region_txt"].unique())
        ],
        value="Middle East & North Africa",
        clearable=False
    ),

    dcc.Graph(id="trend-graph")
])

@app.callback(
    Output("trend-graph", "figure"),
    Input("region-dropdown", "value")
)
def update_graph(selected_region):
    dff = df_year_region[df_year_region["region_txt"] == selected_region]
    fig = px.line(
        dff,
        x="iyear",
        y="attacks",
        title=f"Terrorist Attacks in {selected_region}"
    )
    return fig

if __name__ == "__main__":
    app.run(debug=True)


# In[3]:


import dash
from dash import html, dcc
import plotly.express as px
...

app = dash.Dash(__name__)

...

if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:




