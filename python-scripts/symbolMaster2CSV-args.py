#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import argparse
import sys
import commands
import csv
import os
import json

"""
usage: symbolMaster2CSV.py [-h] [-p] -f FOLDER -s SOURCE -t TARGET

optional arguments:
  -h, --help            show this help message and exit
  -p, --prune           Disable "symid" and "source" info in csv file.
  -f FOLDER, --folder FOLDER
                        The Symbol Folder. Symbol IDs will be read from this
                        folder.
  -s SOURCE, --source SOURCE
                        The Source File with Json Format. Data will be read
                        from this file.
  -t TARGET, --target TARGET
                        The target File with CSV format. Data will be written
                        to this file.

egg.
    python symbolMaster2CSV.py -p -t ./target.csv -s ~/prj2/symbolMaster.json -f /usdata/datafiles/2018/04/25
    
"""

def getArgs():
    parser = argparse.ArgumentParser()  # Creating a parser
    """If encounter -p in command line, args.prune is True; else, args.prune is False."""
    parser.add_argument('-p', '--prune', action='store_true', help='Disable \"symid\" and \"source\" info in csv file.')
    parser.add_argument('-f', '--folder', required=True,
                        help='The Symbol Folder. Symbol IDs will be read from this folder.')
    parser.add_argument('-s', '--source', required=True,
                        help='The Source File with Json Format. Data will be read from this file.')
    parser.add_argument('-t','--target', required=True, help='The target File with CSV format. Data will be written to this file.')
    args = parser.parse_args()
    """ for args, egg.
        Namespace(folder='/usdata/datafiles/2018/04/25', prune=True, source='~/prj2/symbolMaster.json', target='./target.csv')"""
    return args

def readSymIDs(folder):
    assert os.path.isdir(folder)
    return os.listdir(folder)

def sym2str(symbol):
    command = "sym2str {}".format(symbol)
    return commands.getoutput(command)

def readitems(file, symbolids, csvheader):
    """
        file: sourcefile in json format
        itemlist: the table header of CSV file, egg., ["symbolid", "market", "product", "description", "currency"]
        symbolids: symbolids read from folder (specified by -f argument)

        return:
            A symbol info list, with id corresponding to symbolids, and items corresponding to ltemlist
    """
    dictitems = {}
    with open(file, "r") as jsfile:
        line = jsfile.readline()
        while line != "":
            dictsyminfo = json.loads(line)
            syminfo = []
            assert "symid" in dictsyminfo
            if dictsyminfo["symid"] in dictitems:
                line = jsfile.readline()
                continue
            for item in csvheader:
                if item in dictsyminfo:
                    syminfo.append(dictsyminfo[item])
                else:
                    temp = ""
                    if item == "ticker":
                        temp = sym2str(dictsyminfo["symid"])
                    syminfo.append(temp)
            dictitems[dictsyminfo["symid"]] = syminfo
            line = jsfile.readline()

    listitems = []
    for symid in symbolids:
        if int(symid) in dictitems:
            listitems.append(dictitems[int(symid)])
        else:
            print "No information of symbol {}".format(symid)

    return listitems

def writeCSV(targetfile, header, listitems):
    """
    	targetfile: csv file path
    	header: string list
    	listitems: symbol info list to be written
    """
    with open(targetfile, "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for item in listitems:
            writer.writerow(item)

def main():
    args = getArgs()
    symids = readSymIDs(args.folder)
    csvheader = ["symid", "ticker", "market", "source", "name", "currency"]
    if args.prune:
        csvheader = ["ticker", "market", "name", "currency"]
    syminfolist = readitems(args.source, symids, csvheader)
    syminfolist = sorted(syminfolist)
    writeCSV(args.target, csvheader, syminfolist)

if __name__=="__main__":
    sys.exit(main())
