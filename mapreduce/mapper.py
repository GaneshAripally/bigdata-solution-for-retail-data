import sys
import csv

reader = csv.reader(sys.stdin)

# Skip header
next(reader)

for row in reader:
    if len(row) < 9:
        continue

    store_type = row[8]   # Store_Type column
    print(f"{store_type}\t1")
