import json
import random
import math

def get_json():
    data = open_file('export.geojson')
    return data

def open_file(f):
    arquivo = json.loads(open(f, 'r').read())
    return arquivo

def get_three_random_features(arquivo):
    feature = random.sample(arquivo['features'],3)
    return feature

def calc_points(origin, dest):
    x = dest[0] - origin[0]
    y = dest[1] - origin[1]
    return math.sqrt(x*x + y*y)

def compare_distance(first_distance, second_distance):
    return 0 if first_distance < second_distance else 1
