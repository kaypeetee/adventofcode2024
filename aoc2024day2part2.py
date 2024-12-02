from collections import defaultdict

with open("input2.txt", "r") as file:
    lines = file.readlines()

reports = []
for line in lines:
    reports.append(line.split())

totalSafe = 0
totalReports = len(reports)

reportTypes = defaultdict(list)

for i in range(len(reports)):
    report = reports[i]

    for j in range(len(report)):
        if (j == 0):
            reportTypes[i].append(report[j + 1:])
        elif (j == len(report) - 1):
            reportTypes[i].append(report[:j])
        else:
            reportTypes[i].append(report[:j] + report[j + 1:])

for key, value in reportTypes.items():
    penalties = 0
    for rep in value:

        increasing = False
        decreasing = False

        if 0 < int(rep[1]) - int(rep[0]) <= 3:
            increasing = True
        elif 0 > int(rep[1]) - int(rep[0]) >= -3:
            decreasing = True
        else:
            penalties += 1
            continue
        for i in range(2, len(rep)):
            # increasing or decreasing
            diff = int(rep[i]) - int(rep[i - 1])
            if abs(diff) > 3:
                penalties += 1
                break
            elif increasing and diff < 0:
                penalties += 1
                break
            elif decreasing and diff > 0:
                penalties += 1
                break
            elif diff == 0:
                penalties += 1
                break
    if penalties < len(value):
        totalSafe += 1

print(totalSafe)
