import matplotlib.pyplot as plt
import pandas as pd
import csv


def load(file_name):
    places = {}
    with open(file_name) as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            place = row[0]
            weekday = int(row[1])
            time = row[2]
            occupancy = int(row[3])
            if place not in places:
                places[place] = [None for x in range(7)]
            if not places[place][weekday]:
                places[place][weekday] = []
            places[place][weekday].append((time, occupancy))
    return places


def dict_to_pandas(places, place):
    timeDay = [time for time, occupancy in places[place][0]]
    occupancyWeek = []
    for weekday in range(7):
        occupancyDay = []
        for time, occupancy in places[place][weekday]:
            occupancyDay.append(occupancy)
        occupancyWeek.append(occupancyDay)

    pdDataFrame = {'time': timeDay}
    for weekday in range(7):
        pdDataFrame['occupancy' + str(weekday)] = occupancyWeek[weekday]
    return pd.DataFrame(pdDataFrame)


def draw(pandas_data_frame):
    for weekday in range(7):
        plt.plot('time', 'occupancy' + str(weekday), data=pandas_data_frame)
    plt.show()


def main():
    places = load("output.txt")
    places_pandas = dict_to_pandas(places, "arc")
    draw(places_pandas)


if __name__ == "__main__":
  main()
