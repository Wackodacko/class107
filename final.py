import pandas as pd
import csv
from pandas.core.algorithms import take
import plotly.graph_objects as go

df = pd.read_csv("class107.csv")
student_df=df.loc[df["student_id"]=="TRL_987"]
print(student_df.groupby("level")["attempt"].mean())
fig=go.Figure(go.Bar(
    x=student_df.groupby("level")["attempt"].mean(),
    y=["level1","level2","level3","level4"],
    orientation="h"
))
fig.show()
