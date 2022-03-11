#!/usr/bin/python

## Parse the info for a Bitpanda stock using the API

import sys, getopt, requests, json, os.path
import Bitpanda_Info_Parser as BIP
from urllib.request import urlopen

#import pandas as pd

# Source : https://stackoverflow.com/a/34325723
# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """

    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} [{iteration}/{total}] |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def dictPrintTop(dictInput, n):
	if bool(dictInput):
		iterator = 1
		if n <= len(dictInput):
			n = len(dictInput)
		for key, value in dictInput.items():
			print(" -- [{}] -- {} = {} -- {}".format(iterator, key, value[0], value[1]))
			iterator+=1

def allKumo(inputFile, mode):
	# TODO : Multithreading
	# TODO : Use Auto Proxy Rotator
	print("Starting BitPanda Kumo Calculator with input <{}> and mode <{}>...".format(inputFile,mode))
	nTop = 10
	with open(inputFile, 'r') as ticker_list:
		lines = ticker_list.read().splitlines()
		print("Number of tickers to check : {}".format(len(lines)))

	if mode == "all":
		dictionnaries = {"day":{}, "week":{}, "month":{}, "year":{}}
		newDictionnaries = {"day":{}, "week":{}, "month":{}, "year":{}}

		iterator = 1
		length = len(lines)

		print("Calculating Kumos for each ticker in file, for each possible mode..")
		for line in lines:
			printProgressBar(iterator, length, prefix = 'Progress:', suffix = 'Complete', length = 50)
			for mode in ["day", "week", "month", "year"]:
				dictionnaries[mode][line] = BIP.getData(line, mode)
			iterator+=1
		print("-- [number] -- Ticker -- Kumo value -- RSI value")
		for mode in ["day", "week", "month", "year"]:
			print("[info]  Top {} in {} mode :".format(nTop, mode))
			newDictionnaries[mode] = {k: v for k, v in sorted(dictionnaries[mode].items(), key=lambda item: item[1],reverse=True)}
			dictPrintTop(newDictionnaries[mode], 10)
	else:
		dictGeneral = {}
		iterator = 1
		length = len(lines)

		print("Calculating Kumos for each ticker in file with mode {}..".format(inputFile, mode))
		for line in lines:
			printProgressBar(iterator, length, prefix = 'Progress:', suffix = 'Complete', length = 50)
			kumo, rsi = BIP.getData(line, mode)
			dictGeneral[line] = [kumo, rsi]
			iterator+=1

		newDict = {k: v for k, v in sorted(dictGeneral.items(), key=lambda item: item[1],reverse=True)}
		print("-- [number] -- Ticker -- Kumo value -- RSI value")
		print("[info]  Top {} in {} mode :".format(nTop,mode))
		dictPrintTop(newDict, 10)


def argument_selection(argv):
	# Credit : https://www.tutorialspoint.com/python/python_command_line_arguments.htm
	inputFile = 'BitPanda_All_Ticker.txt'
	mode = 'month'

	try:
		opts, args = getopt.getopt(argv,"hi:m:",["help","input=","mode="])
	except getopt.GetoptError:
		print('Usage : BP_Ichimuko.py -i <input>')
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			print('Usage : BP_Ichimuko.py -i <input> -m <mode>')
			print('Default values : input="BitPanda_All_Ticker.txt" ; mode="month"')
			print('Possible modes : "year", "month", "week", "day", "all"')
			sys.exit()
		elif opt in ("-i", "--input"):
			inputFile = arg
		elif opt in ("-m", "--mode"):
			mode = arg

	if os.path.exists(inputFile):
		allKumo(inputFile, mode)
	else :
		print('Error : no input given or non-existent file')
		print('Usage : BP_Ichimuko.py -i <inputFile>')
		sys.exit(2)

if __name__ == "__main__":
	argument_selection(sys.argv[1:])