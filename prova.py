#!/usr/bin/env python3
import csv

def create_csv(row_data):
    with open('useless.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(row_data)