import csv
import math
from datetime import datetime
import pandas as pd
import numpy as np
from bokeh.plotting import figure
from bokeh.io import curdoc



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

            # Skip non-rat/mouse/rodent related complaints
            desc = line['Descriptor'].lower()
            if "rat" not in desc and "rodent" not in desc and "mouse" not in desc:
                continue

            # convert string date to datetime for easy comparison
            created_date = datetime.strptime(line['Created Date'], '%m/%d/%Y %I:%M:%S %p')
            closed_date = datetime.strptime(line['Closed Date'], '%m/%d/%Y %I:%M:%S %p')

            # Check for negative response time
            if created_date > closed_date:
                continue

            #Make sure the location type isn't empty or other
            if not line["Location Type"].strip():
                continue

            if "Other" in line["Location Type"]:
                continue

            key = (line['Location Type'])
            count = complaints.get(key, 0)
            complaints[key] = count + 1


    with open(output_file, 'w') as fo:
        writer = csv.writer(fo)
        writer.writerow(['Location Type', 'Count'])

        for building, count in complaints.items():
            writer.writerow([building, count])

def analyze_data(input_file):
    #read cleaned csv
    df = pd.read_csv(input_file)

    #sort in descending order by count
    df = df.sort_values(by='Count', ascending=False)

    #get the top 6 first
    top7 = df.iloc[:6].copy()
    other_count = df.iloc[6:]['Count'].sum()
    top7.loc[len(top7)] = ["Other", other_count]
    top7['Percentages'] = top7['Count'] / top7['Count'].sum() * 100
    top7['Radians'] = (top7['Percentages'] / 100) * 2 * math.pi
    return top7

def make_graph(df):
    p = figure(x_range=(-1, 2), y_range=(-1, 2), title='Proportion of Rat Incidents by Location Type')

    #We need the angle of each wedge that makes up the pie chart
    rads = df['Radians'].to_numpy()
    #First wedge starts at 0 and goes on until we complete the full 2pi circle
    start_angles = [0]
    prev = start_angles[0]
    for i in rads[:-1]:
        start_angles.append(i+prev)
        prev = i + prev

    #end angles are just the start angles but offset
    end_angles = start_angles[1:] + [2*math.pi]

    #Pie chart settings
    x=0
    y=0
    radius=1
    color=["red", "orange", "yellow", "green", "blue", "pink", "purple"]
    locations = df['Location Type'].to_numpy()
    labels = []
    percents = df['Percentages'].to_numpy()
    for i in range(len(locations)):
        labels.append(f"{locations[i]} ({percents[i]:.1f}%)")
    #plot the chart
    for i in range(len(locations)):
        p.wedge(x, y, radius, start_angle=start_angles[i], end_angle=end_angles[i], color=color[i], legend_label = labels[i])

    curdoc().add_root(p)

def main():
    output_file_name = 'data/task2.csv'
    #clean_data(output_file_name)
    df = analyze_data(output_file_name)
    print(df)
    make_graph(df)

main()