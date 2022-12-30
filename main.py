import pandas as pd

import bokeh
from bokeh.io import curdoc, show, save, output_file
from bokeh.models import Tabs

from os.path import dirname, join

from lineplot import lineplot_tab
from table import table_tab


# Read dataset from file
covid_data = pd.read_csv("./dataset/covid_19_indonesia_time_series_all.csv")

# Preprocessing
covid_data.columns = covid_data.columns.str.replace(" ", "_")
covid_data.columns= covid_data.columns.str.lower()
covid_data['date'] = pd.to_datetime(covid_data['date'], format='%m/%d/%Y')

tab1 = lineplot_tab(covid_data)

# covid_data.groupby("date").count()

tab2 = table_tab(covid_data)
tabs = Tabs(tabs = [tab1, tab2])

curdoc().add_root(tabs)
# show(tabs)
# output_file("final_proj.html")
# save(tabs, "final_proj.html", title="Final")
# show(tabs)