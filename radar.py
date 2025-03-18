
import pandas as pd
import plotly.express as px

donnee = pd.DataFrame(dict(keys=[10,20,30,40], values=["EST","NORD","OUEST","SUD"]))

afficher = px.line_polar(donnee, r="keys", theta="values", line_close=True)
afficher.update_traces(fill="toself")
afficher.show()