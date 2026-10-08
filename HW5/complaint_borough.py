import argparse
from datetime import datetime
import csv

def main():
    parser = argparse.ArgumentParser()
    #create the arguments and flags
    parser.add_argument('-i', '--input', required=True, type=str, help='path to input file')
    parser.add_argument('-s', '--start-date', required=True, type=str, help='start date')
    parser.add_argument('-e', '--end-date', required=True, type=str, help='end date')
    parser.add_argument('-o', '--output', type=str, help='path to output file')
    args = parser.parse_args()

    # convert args to datetime
    start_date = datetime.strptime(args.start_date, '%m/%d/%Y').date()
    end_date = datetime.strptime(args.end_date, '%m/%d/%Y').date()

    # print('processing file', args.input)
    # print('starting date', start_date)
    # print('ending date', end_date)
    # print('output file', args.output)
    # print('---------------------------------------------------------')

    counts = {}

    #open input file
    with open(args.input, 'r') as fi:
        reader = csv.DictReader(fi)

        #go through line by line
        for line in reader:
            #convert string date to datetime for easy comparison
            created_date = datetime.strptime(line['Created Date'], '%m/%d/%Y %I:%M:%S %p').date()

            #check if row is between start and end date
            if created_date >= start_date and created_date <= end_date:
                #make key and increment count
                key = (line['Complaint Type'], line['Borough'])
                counts[key] = counts.get(key, 0) + 1

    #Now output to file if given otherwise just print
    if(args.output != None):
        with open(args.output, 'w') as fo:
            writer = csv.writer(fo)
            writer.writerow(['complaint type', 'borough', 'count'])

            for (complaint, borough), count in counts.items():
                writer.writerow([complaint, borough, count])
    else:
        print("complaint type, borough, count")
        for (complaint, borough), count in counts.items():
            print(f'{complaint},{borough},{count}')


if __name__ == '__main__':
    main()
