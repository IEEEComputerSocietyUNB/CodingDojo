from main import open_file, get_json, get_three_random_features, calc_points, compare_distance
from math import sqrt, pow
import pytest

def test_open_file():
    f = open_file('export.geojson')
    assert isinstance(f, dict)

def test_get_features():
    data = get_json()
    assert isinstance(data['features'], list)
    assert isinstance(data['features'][0]['properties']['name'],str)

def test_get_three_random_features():
    data = get_json()
    features = get_three_random_features(data)
    assert isinstance(features[0]['properties']["name"], str)
    assert len(features) == 3

def test_calc_basic_distance_origin_dest():
    stub_one = ([0.0,0.0], [3.0, 4.0])
    stub_two = ([0.0,0.0], [-3.0, 4.0])
    stub_zero_y = ([0.0,0.0], [-3.0, 0.0])
    stub_zero_x = ([0.0,0.0], [0.0, 4.0])
    origin, dest = stub_one[0], stub_one[1]
    assert calc_points(origin, dest) == 5.0
    origin, dest = stub_two[0], stub_two[1]
    assert calc_points(origin, dest) == 5.0
    origin, dest = stub_zero_y
    assert calc_points(origin, dest) == 3.0
    origin, dest = stub_zero_x
    assert calc_points(origin, dest) == 4.0

def test_calc_not_so_basic_distance_origin_dest():
    stub = ([1.0, 2.0], [3.0, 4.0])
    origin, dest = stub
    assert calc_points(origin, dest) == sqrt(pow((3.0-1.0), 2)+pow((4.0-2.0), 2))

def test_first_is_smallest():
    stub = ([0.0, 0.0], [3.0, 4.0], [5.0, 7.0])
    origin, dest1, dest2 = stub
    assert compare_distance(calc_points(origin,dest1),calc_points(origin,dest2)) == 0

def test_second_is_smallest():
    stub = ([0.0, 0.0], [5.0, 7.0] ,[3.0, 4.0])
    origin, dest1, dest2 = stub
    assert compare_distance(calc_points(origin,dest1),calc_points(origin,dest2)) == 1

def test_fucking_json():
    data = get_json()
    london = data['features'][0]
    wellington = data['features'][1]
    athens = data['features'][2]
    wellington_distance = calc_points(london['geometry']['coordinates'], wellington['geometry']['coordinates'])
    athens_distance = calc_points(london['geometry']['coordinates'], athens['geometry']['coordinates'])

    assert compare_distance(athens_distance, wellington_distance) == 0
