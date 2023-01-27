import csv

total_months = []
net_pnl = 0
list_pnl = []
change_pnl = []

with open("PyBank/Resources/budget_data.csv") as csv_file:
  reader = csv.reader(csv_file)
  header = next(reader)

  for row in reader:
    total_months.append(row[0])
    net_pnl = net_pnl + int(row[1])
    list_pnl.append(int(row[1]))

for num in range(len(list_pnl)-1):
  change_pnl.append(list_pnl[num+1] - list_pnl[num])

length_cpnl = len(change_pnl)
sum_cpnl = sum(change_pnl)
ave_cpnl = sum_cpnl/length_cpnl

print("Financial Analysis")
print("----------------------------")
print("Total Months:", len(total_months))
print("Total:", "$" + str(net_pnl))
print("Average Change: ", "$" + str(round(ave_cpnl,2)))

max_month = change_pnl.index(max(change_pnl)) +1
min_month = change_pnl.index(min(change_pnl)) +1

print("Greatest Increase in Profits: {} (${})".format(total_months[max_month], max(change_pnl)))
print("Greatest Decrease in Profits: {} (${})".format(total_months[min_month], min(change_pnl)))

with open("PyBank/analysis/output.txt","w") as new:
  new.write("Financial Analysis")
  new.write(f"\n")
  new.write("----------------------------")
  new.write(f"\n")
  new.write(f"Total Months: {len(total_months)}")
  new.write(f"\n")
  new.write(f"Total: ${net_pnl}")
  new.write("\n")
  new.write(f"Average Change: ${round(ave_cpnl,2)}")
  new.write(f"\n")
  new.write("Greatest Increase in Profits: {} (${})".format(total_months[max_month], max(change_pnl)))
  new.write(f"\n")
  new.write("Greatest Decrease in Profits: {} (${})".format(total_months[min_month], min(change_pnl)))