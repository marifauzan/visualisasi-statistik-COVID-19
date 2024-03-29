import pandas as pd
import bokeh

from bokeh.plotting import figure
from bokeh.models import HoverTool, ColumnDataSource, RangeSlider, Select, Panel, Dropdown, CustomJS,NumeralTickFormatter
from bokeh.layouts import Column, row, gridplot, widgetbox, column
from datetime import datetime, timedelta

def lineplot_tab(data):
    #Setting source
    source = ColumnDataSource(data={
        'x': data['Date'],
        'y': data['Total Cases'],
        'location': data['Location']})

    #Making line plot
    plot = figure(x_axis_type = "datetime", title = 'Total Cases Indonesia Covid 19', 
                  x_axis_label = 'Date', y_axis_label = 'Total Cases',plot_height=700,
                  plot_width=700)

    # Add the NumeralTickFormatter to the y-axis
    plot.yaxis[0].formatter = NumeralTickFormatter(format='0,0')

    line = plot.line(x='x', y='y', source=source, line_width=1, color='firebrick')
    plot.circle(x='x', y='y', source=source, fill_color="white", line_color="firebrick", size=5)

    hover = HoverTool(
    renderers=[line],
    tooltips=[("Location", "@location"), ("Value", "@y Cases")],
    formatters={'@x': 'datetime'},
    line_policy='nearest',
    mode='mouse')
        
    def style(p):
        p.title.align = 'center'
        p.title.text_font_size = '20pt'
        p.title.text_font = 'sans-serif'
        
        p.xaxis.axis_label_text_font_size = '14pt'
        p.xaxis.axis_label_text_font_style = 'bold'
        p.yaxis.axis_label_text_font_size = '14pt'
        p.yaxis.axis_label_text_font_style = 'bold'

        p.xaxis.major_label_text_font_size = '12pt'
        p.yaxis.major_label_text_font_size = '12pt'

        return p

    def update_plot(attr, old, new):
        x = x_select.value
        y = y_select.value

        if y not in data:
            return

        plot.xaxis.axis_label = x
        plot.yaxis.axis_label = y

        new_data = {
        'x': data[x],
        'y': data[y],
        'location': data['Location']
        }
    
        source.data = new_data

        plot.title.text = '%s Indonesia Covid - 19' % y

    y_select = Select(
        options=['Total Deaths', 'New Cases', 'Total Cases', 'New Deaths'],
        value='New Cases',
        title='Cases')
    y_select.on_change('value', update_plot)

    x_select = Select(
        options=['Date'],
        value='Date',
        title='X Axis')
    x_select.on_change('value', update_plot)

    plot.add_tools(hover)

    plot = style(plot)

    layout = column(y_select, plot)
    tab = Panel(child=layout, title = 'Covid 19 Case Number')
    
    return tab
    
    
    