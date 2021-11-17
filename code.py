import plotly.express as pe
import csv

with open("Tempdata.csv") as csv_file :
    df=csv.DictReader(csv_file)
    fig=pe.scatter(df,x="Temperature",y="Ice-creamSales")
    fig.show()
   