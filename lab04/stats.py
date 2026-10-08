import sys

def average_by_city(total, count, city):
    average = total[city] / count[city]
    return average

def read_valid(line):
    city, temp, date = line.split(";")
    return city, temp, date

def warmest_city(total, count):
    best = ""
    for city in total:
        if best == "" or average_by_city(total, count, city) > average_by_city(total, count, best):
            best = city
    return best