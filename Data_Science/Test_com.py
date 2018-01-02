import csv
import random
import math

with open("Demographic_Statistics_By_Zip_Code.csv", newline='')as infile:
    data = list(csv.reader(infile))

def get_csv_columninstance(header_index):
    value_storage = []
    value_index = data[0].index(header_index)
    for value in data[1:]:
        value_storage.append(value[value_index])
    return value_storage

def check_type(header_index):
    try:
        int_form =([int(i) for i in get_csv_columninstance(header_index)])
        return int_form
    except:
        float_form = ([float(i) for i in get_csv_columninstance(header_index)])
        return float_form

def print_columninstance(header_index):
    for x in check_type(header_index):
        print("%g" % x, end=' ')

def print_rowinstance(primary_key):
    i = 0
    while True:
        if data[i][0] == str(primary_key):
            print(" ".join(data[i]))
            break
        else:
            i += 1

def my_sum(header_index):
    total_sum = sum(i for i in check_type(header_index))
    return total_sum

def my_average(header_index):
    total_average = my_sum(header_index)/len(check_type(header_index))
    return total_average

def my_max(header_index):
    total_max = max(check_type(header_index))
    return total_max

def my_min(header_index):
    total_min = min(check_type(header_index))
    return total_min

def my_deviation(header_index):
    print("\n표본"+"\t\t평균"+"\t\t편차")
    for i in check_type(header_index):
        value_deviation = float(i) - float(my_average(header_index))
        print("%0.2f"%i+"\t\t"+"%0.2f" % my_average(header_index)+"\t\t"+"%0.2f"%value_deviation)

def my_variation(header_index):
    variation_sum = 0
    for i in check_type(header_index):
        variation_sum +=(i-my_average(header_index))**2
    variation_value = variation_sum/len(check_type(header_index))
    return variation_value

def my_standard_variation(header_index):
    std = math.sqrt(my_variation(header_index))
    return std

def my_sorting(header_index):
    ascendant_value = sorted(check_type(header_index), reverse=True)
    sorting_asc = " ".join(str("%g" % i) for i in ascendant_value)
    print(sorting_asc)
    descendant_value = sorted(check_type(header_index))
    sorting_des = " ".join(str("%g" % i) for i in descendant_value)
    print(sorting_des)

# primary_key = input(":")
# print_rowinstance(primary_key)
header_index = input(":")
print(my_deviation(header_index))