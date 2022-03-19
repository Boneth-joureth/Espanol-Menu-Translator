table = [[1,2,3],[4,5,6]]

import csv

# write it
with open('test_file.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    [writer.writerow(r) for r in table]

# read it
with open('test_file.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    table = [[int(e) for e in r] for r in reader]