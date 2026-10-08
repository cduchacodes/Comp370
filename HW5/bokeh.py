import pandas as pd
from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.models import Dropdown
from bokeh.layouts import column


# Helper to return full 12 months, filling missing months with 0.0
def get_monthly_series(zip_val):
    sub = df[df['zip code'] == zip_val].set_index('month')['average']
    return sub.reindex(month_order, fill_value=0.0).tolist()

#Event functions to update the dropdowns and labels
def select_zip1(event):
    if event.item in zip_list:
        dsa.data = {'x': month_order, 'y': get_monthly_series(event.item)}
        dropdown1.label = f'Zipcode 1: {event.item}'
        p.legend.items[0].label = {'value': f'Zipcode: {event.item}'}
    else:
        raise Exception(f'unknown item: {event.item}')

def select_zip2(event):
    if event.item in zip_list:
        dsb.data = {'x': month_order, 'y': get_monthly_series(event.item)}
        dropdown2.label = f'Zipcode 2: {event.item}'
        p.legend.items[1].label = {'value': f'Zipcode: {event.item}'}
    else:
        raise Exception(f'unknown item: {event.item}')


df = pd.read_csv("zip_codes.csv")
# Ensure clean string representation for zip codes
df['zip code'] = df['zip code'].astype(str).str.strip()

month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

#get the "menu"
zip_list = sorted([str(z).strip() for z in df['zip code'].dropna().unique()
    if str(z).strip() not in ('ALL', 'nan', '')])

#Make the graph
p = figure(x_range=month_order, y_range=(0, max(df['average'])*1.1),
           title='Average Zip Code Service Times vs Overall Average Time',
           x_axis_label='Month', y_axis_label='Average Zip Code Service Times (Hours)')

#Add the lines and their default values
a = p.line(month_order, get_monthly_series('11218'), color='red', legend_label='Zipcode 1')
b = p.line(month_order, get_monthly_series('10466'), color='blue', legend_label='Zipcode 2')
r = p.line(month_order, get_monthly_series('ALL'), color='black', legend_label='ALL 2020 data')
dsa = a.data_source
dsb = b.data_source

#Make the dropdowns
dropdown1 = Dropdown(label='select zip code 1', menu=zip_list)
dropdown2 = Dropdown(label='select zip code 2', menu=zip_list)
dropdown1.on_event('menu_item_click', select_zip1)
dropdown2.on_event('menu_item_click', select_zip2)

#Add to curdoc so it can show up on the dashboard
curdoc().add_root(column(dropdown1, dropdown2, p))
