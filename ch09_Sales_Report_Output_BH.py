#Brian Herrera
#ch09 Sales Report
#10/4/2024
#Creates program that dymanically displays report of sales by quarter for a company
#with four sales regions. Also have to use formatting to print out values.

import locale
locale.setlocale(locale.LC_ALL, "us")

sales = [[1540.0, 2010.0, 2450.0, 1845.0], # Region 1
        [1130.0, 1168.0, 1847.0, 1491.0], # Region 2
        [1580.0, 2305.0, 2710.0, 1284.0], # Region 3
        [1105.0, 4102.0, 2391.0, 1576.0]] # Region 4

print("Total sales by region:")
counter = 1
for row in sales:
    salesTotal = sum(row)
    print(f"Region {(counter)}: {locale.currency(salesTotal, grouping=True)}")
    counter += 1
print()


print("Total sales by quarter:")
counter = 1
for column in range(4):
    quarterTotal = sum(row[column] for row in sales)
    print(f"Region {(counter)}: {locale.currency(quarterTotal, grouping=True)}")
    counter += 1
print()


total_sum = 0
for row in sales:
    for total in row:
        total_sum += total
print(f"Total annual sales, all regions:\n{locale.currency(total_sum, grouping = True)}")

    
