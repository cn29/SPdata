import csv
import pprint
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

# a collection of weekly stored data
class WeekData:
    def __init__(self):
        self.weekday = [[] for _ in range(7)]
        self.weekday_ave = []
        self.weekSD = 1.1

    def ave_std(self):
        self.weekday_ave = [float(sum(l)) / len(l) for l in self.weekday]
        self.weekSD = np.std(self.weekday_ave)


class Element:
    def __init__(self):
        self.seasons = [WeekData() for _ in range(4)]
        self.year = WeekData()

    def season_sd(self):
        return [self.seasons[i].weekSD for i in range(4)]


# read data from csv
data = []
with open('SP+S.csv') as csvFile:
    readCSV = csv.reader(csvFile, delimiter=',')
    for row in readCSV:
        data.append(row)


N = len(data[0])-2                              # number of elements
elements = [Element() for _ in range(N)]        # build data container

# iterate over all elements
for i in range(1, N):
    print("Element %s", i)
    for row in data:
        if row[1] == '' or row[i+1] == '':      # check if the data is valid
            continue
        day = int(row[1])
        value = float(row[i+1])

        # by seasons
        date = row[0].split('/')
        rem = int(date[0]) % 12
        sea_num = rem // 3                   # indicates which season is the date in
        elements[i].seasons[sea_num].weekday[day - 1].append(value)          # store the data into three days
        elements[i].seasons[sea_num].weekday[day % 7].append(value)
        elements[i].seasons[sea_num].weekday[(day+1) % 7].append(value)

        # all year
        elements[i].year.weekday[day - 1].append(value)  # store the data into three days
        elements[i].year.weekday[day % 7].append(value)
        elements[i].year.weekday[(day + 1) % 7].append(value)

    # compute average & SD
    for sea_num in range(4):
        elements[i].seasons[sea_num].ave_std()
    elements[i].year.ave_std()
    print(elements[i].seasons[0].weekday_ave)
    print(elements[i].seasons[0].weekSD)

# write to csv
save_csv = True
if save_csv:
    with open('result.csv', 'w') as target:
        wr = csv.writer(target)
        title_row = [' ', 'Winter', 'Sprint', 'Summer', 'Fall']
        wr.writerow(title_row)
        for i in range(1, N):
            row = elements[i].season_sd()
            row.insert(0, i)
            wr.writerow(row)
