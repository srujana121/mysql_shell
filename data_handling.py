#!/usr/bin/python
import sys,re
import argparse, csv
from display import error_handling
""" data handlig involves reading metafiles ,sotring table info and storing tables' data"""

#metadata file

def reading_metadata(filename):
    try:
        metadata_file=open(filename,'r')
        title=""
        tables={}
        h=0
        for line in metadata_file:
            line=line.strip()  #to remove extra spaces
            if line =='<begin_table>':
                h=1
            elif h==1:
                tables[line]=[]
                title=line
                h=-1
            elif h==-1 and line!='<end_table>':
                tables[title].append(line)
        return tables
    except IOError:
        error_handling('No metadata file \'' + filename + '\' found')

#reading tables

def reading_tables(title):
    table_filename= title + '.csv'
    table_data=[]
    try:
        with open (table_filename,'r') as table_file:
            data=csv.reader(table_file, delimiter=',')
            for row in data:
                table_data.append(row)
            return table_data
    except IOError:
        error_handling('ERROR: Table \'' + title + '\' doesn\'t exists')


