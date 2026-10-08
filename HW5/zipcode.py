import csv
from datetime import datetime

def main():
    times = {}

    #open input file
    with open("hw5.csv", 'r') as fi:
        reader = csv.DictReader(fi)

        #go through line by line
        for line in reader:
            # Check if closed otherwise skip
            if line['Closed Date'].strip() == "":
                continue

            # Check for zipcode otherwise skip
            if line['Incident Zip'].strip() == "":
                continue

            #convert string date to datetime for easy comparison
            created_date = datetime.strptime(line['Created Date'], '%m/%d/%Y %I:%M:%S %p')
            closed_date = datetime.strptime(line['Closed Date'], '%m/%d/%Y %I:%M:%S %p')

            #Check for negative response time
            if created_date > closed_date:
                continue

            #Now we've passed all the checks for the line so we can update the averages (Zip and overall)
            resolution_time = closed_date - created_date
            hours = resolution_time.total_seconds() / 3600
            month = created_date.strftime('%B')

            key = (line['Incident Zip'].strip(), month)
            total_time, count = times.get(key, (0.0,0))
            times[key] = (total_time + hours, count + 1)

            key2 = ("ALL", month)
            t_time, c = times.get(key2, (0.0, 0))
            times[key2] = (t_time + hours, c + 1)

    with open("zip_codes.csv", 'w') as fo:
        writer = csv.writer(fo)
        writer.writerow(['zip code', 'month', 'average'])

        for (zip, month), (total, count) in times.items():
            writer.writerow([zip, month, total/count])


if __name__ == '__main__':
    main()
