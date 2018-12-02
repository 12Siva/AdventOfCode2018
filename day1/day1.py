from collections import defaultdict

file = open("input.txt","r")

frequency_changes = []
for line in file:
    frequency_changes.append(int(line))

counter = 0

seen_frequencies = defaultdict(int)
seen_frequencies[counter] += 1
found = False

while not found:
    for element in frequency_changes:
        counter += element
        if seen_frequencies[counter] == 1:
            print("FIRST: " + str(counter))
            found = True
            break
        else:
            seen_frequencies[counter] += 1
