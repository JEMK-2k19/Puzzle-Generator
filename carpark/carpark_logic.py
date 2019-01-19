from django.shortcuts import render
import csv, io
from . import api

# Create your views here.
def read_csv(fname):
    new = []
    with open(fname, encoding = 'utf-8') as f:
        for row in csv.reader(f):
            new.append(row)
    return new

def get_distance(src, dst):
    return ((src[0] - dst[0]) ** 2 + (src[1] - dst[1]) ** 2) ** 0.5

def find_nearest_carpark(place):
    coords = api.to_coord(place)
    carparks = list_of_carparks()
    max_dist = 10000000000
    best = 0
    for c in carparks:
        carpark_coord = c.get_coords()
        dist = get_distance(coords, carpark_coord)
        if dist < max_dist:
            max_dist = dist
            best = c
            #print(best.address)
    return best.address

def list_of_carparks():
    data = read_csv("carpark/hdb-carpark-information.csv")[1:98]
    carparks = []
    for row in data:
        newCarpark = Carpark(row)
        carparks.append(newCarpark)
    return carparks

class Carpark:
    def __init__(self, row):
        self.car_park_no = row[0]
        self.address = row[1]
        self.x_coord = float(row[10])
        self.y_coord = float(row[9])
        #self.x_coord = float(row[2]) * (9.02612061674652 * (10 ** -6)) + 1#.01708687143698
        #self.y_coord = float(row[3]) * (8.95286593891225 * (10 ** -6)) + 103#.5824577
        self.car_park_type = row[4]
        self.type_of_parking_system = row[5]
        self.short_term_parking = row[6]
        self.free_parking = row[7]
        self.night_parking = row[8]

    def get_coords(self):
        return (self.y_coord, self.x_coord)

def carpark_view(request):
    carparks = list_of_carparks()
    return render(request, 'carpark/carpark.html', {'carparks': carparks})

def write(output_name, result):
    ofile = io.open(output_name, 'w', newline='', encoding='utf-32')
    with ofile:
        writer = csv.writer(ofile, delimiter=",")
        writer.writerows(result)
    ofile.close()

print(find_nearest_carpark("ang mo kio hub"))


# results = []
# for c in list_of_carparks()[:100]:
#     try:
#         results.append(list(api.to_coord(c.address)))
#     except:
#         results.append([])
# write("output.csv", results)