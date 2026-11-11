import argparse
import csv
import json
import random

def clean_title(title):
    #replace tabs, new lines, and returns with a space so it doesn't mess with tsv
    return title.replace("\t", " ").replace("\n", " ").replace("\r", " ")

def load_json(path):
    # open given json file
    with open(path) as json_file:
        data = json.load(json_file)

    arr = []
    for item in data['data']['children']:
        temp = [item['data']['name'], clean_title(item['data']['title'])]
        arr.append(temp)

    return arr


def main():
    parser = argparse.ArgumentParser()

    #create the arguments and flags
    parser.add_argument('-o', required=True, type=str, help='path to output file')
    parser.add_argument('--seed', required=False, type=int, help='optional int for seed')
    parser.add_argument('json_file', type=str, help='paht to the input json file')
    parser.add_argument('num_posts_to_output', type=int, help='number of posts to output')

    args = parser.parse_args()

    #set seed if it was given
    if args.seed != None:
        random.seed(args.seed)

    json_arr = load_json(args.json_file)

    #open output file
    with open(args.o, 'w') as outfile:
        writer = csv.writer(outfile, delimiter='\t')
        writer.writerow(['Name', 'title', 'coding'])

        # check if num_posts_to_output is greater than 100 (the max we have) if so, output everything
        if args.num_posts_to_output >= 100:
            for name, title in json_arr:
                writer.writerow([name, title, ''])
        #otherwise use the random sampling without replacement
        else:
            for i in range(args.num_posts_to_output):
                index = random.randint(0, len(json_arr) - 1)
                writer.writerow([json_arr[index][0], json_arr[index][1], ''])
                json_arr.pop(index)





if __name__ == '__main__':
    main()
