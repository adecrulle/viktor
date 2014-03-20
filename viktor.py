#!/usr/bin/env python
#-*-coding:utf-8 -*

import numpy
import argparse
import csv
import itertools
from pylab import *
import matplotlib.pyplot as plt

lines={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}

parser = argparse.ArgumentParser(description='Analyze kinetics data from Viktor')
parser.add_argument("--input", type=str, help="input file")
parser.add_argument("--output", type=str, help="output file")

args = parser.parse_args()

table = csv.reader(open(args.input,'rU')) 
    

# We first parse the CSV files to get two numpy arrays, od_table and fluo_table

wells=dict()
for (nl,row) in enumerate(table):
    if nl==0:
        continue
    namewell=row[2]
    value=row[5]
    if wells.has_key(namewell):
        wells[namewell].append(value.replace(',','.'))
    else:
        wells[namewell]=[value.replace(',','.')]

allvalues=list(itertools.chain(*wells.values()))
ymin=float(min(allvalues))
ymax=float(max(allvalues))

f, axarr = plt.subplots(8, 12)
for well in wells.keys():
    y=lines[well[0]]
    x=int(well[1:])-1
    axarr[y,x].plot(wells[well],'b')
    #plt.xlim(xmin,xmax)
    axarr[y,x].set_ylim((ymin,ymax))

plt.savefig(args.output)