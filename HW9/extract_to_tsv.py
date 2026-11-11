import argparse
import csv
import json
import random
import pandas as pd
import numpy as np


def clean_title(title):
    #replace tabs, new lines, and returns with a space so it doesn't mess with tsv
    return title.replace("\t", " ").replace("\n", " ").replace("\r", " ")

def load_json(path):
    # open given json file
    with open(path) as json_file:
        data = json.load(json_file)

    arr = []
    for item in data['data']:
        temp = [item['name'], clean_title(item['title'])]
        arr.append(temp)
    return arr

def exclude_names(paths):
    arr = []
    for path in paths:
        with open(path) as tsv_file:
            df = pd.read_csv(tsv_file, sep='\t')
            arr = np.append(arr, df['Name'].to_numpy())
    return arr


def main():
    parser = argparse.ArgumentParser()

    #create the arguments and flags
    parser.add_argument('-o', required=True, type=str, help='path to output file')
    parser.add_argument('--seed', required=False, type=int, help='optional int for seed')
    parser.add_argument('--exclude', action='append', default=[], help='TSV files with posts to exclude')
    parser.add_argument('json_file', type=str, help='paht to the input json file')
    parser.add_argument('num_posts_to_output', type=int, help='number of posts to output')

    args = parser.parse_args()

    #set seed if it was given
    if args.seed != None:
        random.seed(args.seed)

    json_arr = load_json(args.json_file)
    #Now figure out what names to exclude
    exclude_arr = exclude_names(args.exclude)

    # Now remove those names
    # Convert to a set for fast O(1) membership lookups
    exclude_set = set(exclude_arr)

    # Filter the 2D array
    filtered_data = [row for row in json_arr if row[0] not in exclude_set]
    print('Number of excluded posts: ', len(json_arr)-len(filtered_data))

    #open output file
    with open(args.o, 'w') as outfile:
        writer = csv.writer(outfile, delimiter='\t')
        writer.writerow(['Name', 'title', 'coding'])

        # check if num_posts_to_output is greater than 100 (the max we have) if so, output everything
        if args.num_posts_to_output >= len(filtered_data):
            for name, title in filtered_data:
                writer.writerow([name, title, ''])
        #otherwise use the random sampling without replacement
        else:
            for i in range(args.num_posts_to_output):
                index = random.randint(0, len(filtered_data) - 1)
                writer.writerow([filtered_data[index][0], filtered_data[index][1], ''])
                filtered_data.pop(index)

if __name__ == '__main__':
    main()
