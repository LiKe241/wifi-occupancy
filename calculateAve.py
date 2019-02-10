import csv
import datetime

places = {}
with open("HackDavis 2019_Wifi Data_Wifi-TotalCount-1Jan19-7Feb19.txt") as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        place = row[9]
        date = datetime.datetime(int(row[3]), int(row[4]), int(row[5]))
        time = datetime.time(int(row[6]), int(row[7]))
        if place not in places:
            places[place] = {}
        if date not in places[place]:
            places[place][date] = {}
        places[place][date][time] = int(row[10])

for place, dates in places.items():
    sumWeekday = [{} for x in range(7)]
    countWeekday = [0 for x in range(7)]
    aveWeekday = {}
    for date, timeline in dates.items():
        weekday = date.weekday()
        for time, occupancy in timeline.items():
            if time not in sumWeekday[weekday]:
                sumWeekday[weekday][time] = 0
            sumWeekday[weekday][time] += occupancy
        countWeekday[weekday] += 1
    places[place]["weeklyAve"] = [{} for x in range(7)]
    for weekday in range(7):
        for time, occupancy in sumWeekday[weekday].items():
            places[place]["weeklyAve"][weekday][time] = occupancy / countWeekday[weekday]

with open("output.txt", 'w') as outFile:
    csvWriter = csv.writer(outFile)
    for place in places.keys():
        for weekday in range(7):
            for time, occupancy in sorted(places[place]["weeklyAve"][weekday].items()):
                csvWriter.writerow([place, weekday, time, occupancy])

