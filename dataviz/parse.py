"""Data Viz Project

Parse data from CSV or Excel, render it in JSON and save to database, then visualize in graph form

Copyright (c) 2013 E. Lynn Root

"""

import csv

MY_FILE = "sample_sfpd_incident_all.csv"

def csv2json(raw_file, delimiter=","):
    """Parses raw CSV file and returns JSON-like object."""
    #Open the CSV file and read the data
    with open(raw_file) as file:
        data = csv.reader(file,delimiter=delimiter)
        header = next(data)
        #Build the JSON-like data structure
        parsed = [dict(zip(header,row)) for row in data]
    return parsed


if __name__ == "__main__":
    filename = input("Enter filename to parse: ")
    try:
        for line in csv2json(filename):
            print(line)
    except:
        print("Could not find the file, or found the file but could not parse. \nExiting...")
        exit(0)
