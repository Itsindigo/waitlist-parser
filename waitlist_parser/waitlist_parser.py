import os
import sys
from csv import DictReader, DictWriter

if __name__ == "__main__":
    if len(sys.argv) > 1:
        my_file = sys.argv[-1]
    else:
        print("File path not provided")
        sys.exit(1)

    _, extension = os.path.splitext(my_file)
    if extension != '.csv':
        print("This script accepts CSV Filetypes only.")
        sys.exit(1)

    with open(my_file) as csvfile:
        records = []
        waitlist = DictReader(csvfile)
        for row in waitlist:
            records.append(row)

    column_headers = records[0].keys()

    input = raw_input('Enter the column header you would like to split: \n')

    if input not in column_headers:
        print("Input supplied not in column headings.... exiting.")
        sys.exit(1)

    for record in records:
        target = record[input]
        split_names = target.split(' ')
        del record[input]
        record['first %s' % input] = split_names[0]
        record['last %s' % input] = ''
        if len(split_names) > 1:
            record['last %s' % input] = ' '.join(split_names[1:])

    with open('outfiles/waitlist.csv', 'w') as outfile:
        writer = DictWriter(outfile, records[0].keys())
        writer.writeheader()
        writer.writerows(records)