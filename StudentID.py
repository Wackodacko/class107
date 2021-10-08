import pandas as pd
import csv
import plotly.graph_objects as go
from pandas.core import groupby 

df = pd.read_csv("class107.csv")
print(df.groupby("level")["attempt"].mean())

fig = go.Figure(go.Bar(
    x=df.groupby("level")["attempt"].mean(),
    y=["level1","level2","level3","level4"],
    orientation="h"  
))
fig.show()
