import plotly.express as pe
import csv

with open("coffee.csv") as csv_file :
    df=csv.DictReader(csv_file)
    fig=pe.scatter(df,x="Coffeeinml",y="sleepinhours")
    fig.show()
   