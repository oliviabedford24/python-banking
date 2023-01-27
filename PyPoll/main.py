import csv

output = open("output.txt","w")

total_count = 0
ddd = dict()

with open("PyPoll/election_data.csv") as csv_file:
  reader = csv.reader(csv_file)
  header = next(reader)
  
  for row in reader:
    total_count = total_count + 1
    candidate_name = row[2]
    if candidate_name in ddd.keys():  
      ddd[candidate_name] = ddd[candidate_name] + 1
    else:
      ddd[candidate_name] = 1

print("Election Results")
print("-------------------------")
print("Total Votes:", total_count)
print("-------------------------")
for key, value in ddd.items():
  print(key + ": {:.3f}% ({})".format((value/total_count)*100, value))
print("-------------------------")

winner = None
winner_count = None
for key, value in ddd.items():
  if winner_count is None or value > winner_count:
    winner = key
    winner_count = value

print("Winner:", winner)
print("-------------------------")

output.write("Election Results")
output.write(f"\n")
output.write("-------------------------")
output.write(f"\n")
output.write(f"Total Votes: {total_count}")
output.write(f"\n")
output.write("-------------------------")
output.write(f"\n")
for key, value in ddd.items():
  output.write(key + ": {:.3f}% ({})".format((value/total_count)*100, value))
  output.write(f"\n")

output.write("-------------------------")
output.write(f"\n")
output.write(f"Winner: {winner}")
output.write(f"\n")
output.write("-------------------------")