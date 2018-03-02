import csv
import matplotlib.pyplot as plt
import numpy as np

# read data from csv
data = []
with open('C:/Users/weixu/Google Drive/Wei/Research/python3/project1/data/EO-fall.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        data.append(row)

N = len(data[0])-2
# compute average
week_ave = []
# iterate over all elements
for i in range(1,17):
    weekday = [[]] * 7      # initialize the size
    j = 0
    for row in data:
        if row[1] == '' or row[i+1] == '':      # check if the data is valid
            continue
        day = int(row[1])
        value = float(row[i+1])
        weekday[day - 1].append(value)      # store the data into three days
        weekday[day % 7].append(value)
        weekday[(day+1) % 7].append(value)

    average = np.mean(weekday, axis=1)
    week_ave.append(average)
    if i==7:
        print(np.matrix(weekday))

print(week_ave)
#week = list(range(1, 8))
#plt.plot(week, average)
#plt.show()

# write to csv
save_csv = True
if save_csv:
    with open('C:/Users/weixu/Google Drive/Wei/Research/python3/project1/data/EO-fall absolute.csv', 'w') as target:
        wr = csv.writer(target)
        for row in week_ave:
            wr.writerow(row)
