# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(list_of_lists, csvpath, header):
    """Saves the data to a CSV file.

    Args:
        A list of lists that contains the rows of data
        Future csvpath
        Headers, if applied
    """
    
    
    with open(csvpath, 'w', newline = '') as csvfile:
        
        csvwriter = csv.writer(csvfile)
        
        csvwriter.writerow(header)
        
        for row in list_of_lists:
            csvwriter.writerow(row)
    print("Writing complete")