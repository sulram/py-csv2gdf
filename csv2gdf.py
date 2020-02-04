#!/usr/bin/env python

import csv
import util
import re

from optparse import OptionParser
from gdf_formatter import Graph

graph = Graph()
links = dict()

def saveLink(node1, node2, w):
    key = node1 + "_" + node2
    if key in links:
        links[key] += w
    else:
        links[key] = w


def readCSV(file):

    with open(file) as csvfile:

        reader = csv.DictReader(csvfile)

        count = 0

        for row in reader:

            count += 1

            #user = row['username'].decode('utf-8')

            words = util.tokenize(row['tweet'])

            for word in words:
                for other_word in words:
                    if word != other_word:
                        saveLink(word, other_word, 0.1)
            

            print('count %d edges %d' % (count, len(links)))
    
        skip = 0
        relevant = 0

        for k, v in links.items():
            nodes = k.split('_')
            if v > 0.4:
                tryAddNode(nodes[0])
                tryAddNode(nodes[1])
                tryAddLink(nodes[0], nodes[1])
                relevant += 1
            else:
                skip += 1

            print((skip,relevant))
    
    print('saving...')
    graph.dump(output_file='output.gdf')
    print('done!')


def tryAddNode(n):
    try:
        graph.addNode(name=n)
    except ValueError:
        pass

def tryAddLink(n1,n2):
    try:
        graph.addLink(node1=n1, node2=n2)
    except:
        pass

def main():
    parser = OptionParser(usage="usage: %prog [options] filename",
                          version="%prog 1.0")
    parser.add_option("-f", "--filename",
	    action="store", # optional because action defaults to "store"
	    dest="filename",
	    default=False,
	    help="the CSV file to process",)
    (options, args) = parser.parse_args()

    if(options.filename):
        readCSV(options.filename)

    else:
        print('no file selected')

if __name__ == '__main__':
    main()
