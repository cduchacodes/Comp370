import csv
from datetime import datetime
import pandas as pd
import numpy as np
from bokeh.plotting import figure
from bokeh.io import curdoc


month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def clean_data(output_file):
    complaints = {}

    # open input file
    with open("../HW5/hw5.csv", 'r') as fi:
        reader = csv.DictReader(fi)

        # go through line by line
        for line in reader:
            # Check if closed otherwise skip
            if line['Closed Date'].strip() == "":
                continue

            # Skip non-noise related complaints
            if "Noise" not in line['Complaint Type']:
                continue

            # convert string date to datetime for easy comparison
            created_date = datetime.strptime(line['Created Date'], '%m/%d/%Y %I:%M:%S %p')
            closed_date = datetime.strptime(line['Closed Date'], '%m/%d/%Y %I:%M:%S %p')

            # Check for negative response time
            if created_date > closed_date:
                continue

            # Now we've passed all the checks for the line so we can update the count for the cause and the month
            month = created_date.strftime('%B')

            key = (line['Descriptor'], month)
            count = complaints.get(key, 0)
            complaints[key] = count + 1


    with open(output_file, 'w') as fo:
        writer = csv.writer(fo)
        writer.writerow(['Cause', 'Month', 'Count'])

        for (desc, mon), count in complaints.items():
            writer.writerow([desc, mon, count])

def find_most_common(input_file):
    #Read the cleaned file with the data
    df = pd.read_csv(input_file)

    #Now we want to find the top 3 causes of noise for each month

    #get the right order of the months
    df["Month"] = pd.Categorical(df["Month"], categories=month_order, ordered=True)
    new_df = df.sort_values(by=["Month", "Count"], ascending=[True, False]).groupby("Month", observed=False).head(3)

    #return the dataframe with only the data we need to make the graph
    new_df.to_csv("data/task12.csv", index=False)
    return new_df

# Helper to return full 12 months for a given cause
def get_monthly_series(df, cause):
    sub = df[df['Cause'] == cause].set_index('Month')
    return sub.reindex(month_order)["Count"].fillna(0).to_numpy()

def make_graph(df):
    causes = ["Loud Music/Party", "Banging/Pounding", "Loud Talking"]

    # Make the graph
    p = figure(x_range=month_order, height=450, width=850, title='Top 3 Noise Complaints by Month',
               x_axis_label='Month', y_axis_label='Frequency of Noise Complaint')
    # Add the three stacked bars one at a time

    # Get the top and bottom levels for the biggest bar at the bottom
    start = np.zeros(len(month_order))
    stop = get_monthly_series(df, causes[0])
    bottom_bar = p.vbar(
        x=month_order,
        width=0.7,
        bottom=start,
        top=stop,
        color="red",
        legend_label=causes[0],
    )

    # Get new levels
    start = stop
    stop = start + get_monthly_series(df, causes[1])
    middle_bar = p.vbar(
        x=month_order,
        width=0.7,
        bottom=start,
        top=stop,
        color="orange",
        legend_label=causes[1],
    )

    # Get last levels
    start = stop
    stop = start + get_monthly_series(df, causes[2])
    top_bar = p.vbar(
        x=month_order,
        width=0.7,
        bottom=start,
        top=stop,
        color="yellow",
        legend_label=causes[2],
    )

    p.legend.location = "top_left"
    p.legend.click_policy = "mute"

    # Add to curdoc so it can show up on the dashboard
    curdoc().add_root(p)


def main():
    clean_file_name = "data/task1.csv"
    #clean_data(clean_file_name)
    df = find_most_common(clean_file_name)
    make_graph(df)

main()

