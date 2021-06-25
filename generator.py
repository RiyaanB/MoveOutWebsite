import csv

rows = []

with open('selloff.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t Item {row[0]} which is {row[1]} has price {row[2]}.')
            rows.append((row[0], row[1], row[2]))
            line_count += 1
    print(f'Processed {line_count} lines.')

file = open("index_template.html", "r")
index_html = file.read()
file.close()

file = open("item_div.html", "r")
item_div_html = file.read()
file.close()


items = ""

for row in rows:
    item = item_div_html.format(row[0], row[0], row[1], row[2])
    items += item + "\n"



file = open("index.html", "w")
file.write(index_html.format(items))
file.close()

exit()