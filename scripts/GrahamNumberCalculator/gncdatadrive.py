# work in progress
from pathlib import Path
import csv
import math
import json
import os
import numpy as np

inputdatafilepath = Path(
    ".\scripts\GrahamNumberCalculator\Data\Input\gncDatafile.csv")  # define input file path
outputdatafilepath = Path(
    ".\scripts\GrahamNumberCalculator\Data\Output\gnc-outputDatafile.csv")  # define output file path

inputdata = []  # declare data to input csv file
stockdata = []  # declare data from input csv file


def jsonparser():

    folder_path = 'scripts/SimpleAlphaVantageCacher/output/json_cache/DATA'
    inputdata = np.empty((1, 4))
    print(inputdata)
    for filename in os.listdir(folder_path):

        if filename.endswith('CompanyOverview.json'):
            file_path = os.path.join(folder_path, filename)
            file_base_name = filename.split('.', 1)
            # inputdata.append(file_base_name[0])[0]

            compname = file_base_name[0]
            # print(file_base_name[0])
            try:
                with open(file_path) as json_file:
                    json_data = json.load(json_file)
                    # Access the data in the JSON file
                    try:
                        eps = json_data["EPS"]
                        if eps.isdigit():
                            eps = float(eps)
                        bvps = json_data["BookValue"]
                        if bvps.isdigit():
                            bvps = float(bvps)

                        # Add a new row to the array
                        new_row = np.array([[compname, "null", eps, bvps]])
                        inputdata = np.concatenate(
                            (inputdata, new_row), axis=0)
                    except KeyError:
                        print(
                            'The key "eps" was not found in the {compname} JSON object')
                    # print(inputdata)
            except json.JSONDecodeError:
                print(f"Skipping {file_name} because it is empty")
                continue
    write_data_to_csv(inputdata, inputdatafilepath)


def read_data_from_csv(stockdata):
    with open(inputdatafilepath, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader, None)  # skip the headers
        for row in csv_reader:
            # store the first four columns of each row
            stockdata.append(row[0:4])
            # print(data)
        # for row in stockdata:
            # print(row)
        return stockdata

    # Close the CSV file
    file.close()


def write_data_to_csv(data, filepath):

    if filepath == inputdatafilepath:
        header = ['StockName', 'StockPrice', 'Earn_Value_Per_Share',
                  'Book_Value_Per_Share']  # Define header as an array
    else:
        header = ['StockName', 'StockPrice', 'Earn_Value_Per_Share',
                  'Book_Value_Per_Share', 'GrahamNumber']  # Define header as an array
    # Open the CSV file in write mode
    with open(filepath, 'w', newline='') as csv_file:

        # Create a csv.writer object to write to the CSV file
        writer = csv.writer(csv_file)

        writer.writerow(header)  # Write header row to file

        # Iterate over the list and write each element to the CSV file
        for row in data:
            writer.writerow(row)
    # Close the CSV file
    csv_file.close()


def graham_number():

    jsonparser()

    read_data_from_csv(stockdata)  # call csv read function

    multiplier = 22.5  # define multiplier value for Graham Number Calculation

    for row in stockdata:  # iterate through all the rows of csv file to capture eps & bvps

        try:
            earn_value_per_share = float(row[2])  # store eps in a variable
            book_value = float(row[3])  # store bvps in a variable
        except:
            earn_value_per_share = (row[2])  # store eps in a variable
            book_value = (row[3])  # store bvps in a variable

        if isinstance(earn_value_per_share, str) or isinstance(book_value, str):  # Skip strings
            continue
        elif (earn_value_per_share) < 0 or (book_value) < 0:  # Skip Negative Value
            continue
        else:
            # calculate graham number using the formulae
            graham_number = round(
                math.sqrt(multiplier * earn_value_per_share * book_value), 2)
            print(graham_number)
        # append calculated graham number value to each row
            row.append(graham_number)
    # print(stockdata)
    # call function to wtite the input stock values and graham number to output csv file

    write_data_to_csv(stockdata, outputdatafilepath)


graham_number()
