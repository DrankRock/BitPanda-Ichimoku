#!/usr/bin/python

## Parse the info for a Bitpanda stock using the API

import sys, getopt, requests, json
from urllib.request import urlopen
#import pandas as pd

def getData(entry, mode):

	if mode == "day":
		url = "https://api.bitpanda.com/v2/ohlc/usd/day?assets="+entry
	elif mode == "week":
		url = "https://api.bitpanda.com/v2/ohlc/usd/week?assets="+entry
	elif mode == "month":
		url = "https://api.bitpanda.com/v2/ohlc/usd/month?assets="+entry
	elif mode == "year":
		url = "https://api.bitpanda.com/v2/ohlc/usd/year?assets="+entry
	else:
		print("ERROR : Unknown mode, choose between day, week, month, year")
		sys.exit(2)

	responseJson = requests.get(url).json()
	jsonData = json.loads(json.dumps(responseJson))
	iterator = 1
	number_of_data = len(jsonData['data'][entry])

	# ---- RSI
	# Arbitrary choice of a 14 periods value
	previous_close_value = -1
	U = []
	D = []
	sumU = 0
	sumD = 0
	number_of_periods = 0
	if number_of_data <= 14:
		RSI_periods = number_of_data-1
	else:
		RSI_periods = 14
	RSI_start = number_of_data - RSI_periods		

	# ---- Tenkan
	tenkan_max = -1
	tenkan_min = 9999999999

	# ---- Senkou
	senkou_max = -1
	senkou_min = 9999999999

	# ---- Kijun
	kijun_max = -1
	kijun_min = 9999999999

	# ----
	if number_of_data < 60:
		senkou_value = 0
		kijun_value = number_of_data/2
		tenkan_value = number_of_data - number_of_data/6
	else:
		senkou_value = number_of_data - 60
		kijun_value = number_of_data - 30
		tenkan_value = number_of_data - 9

	
	# ---- DEBUG VALUES
	number_of_kijun = 0
	number_of_tenkan = 0
	number_of_senkou = 0

	for line in jsonData['data'][entry]:
		closeData = line['attributes']['close']
		dateData = line['attributes']['time']['unix']
		#print(closeData,", ",dateData)
		closeData = float(closeData)

		## Relative Strength Index
		if iterator> RSI_start:
			number_of_periods+=1
			differenceValue = closeData - previous_close_value
			if differenceValue > 0:
				uValue = differenceValue
				dValue = 0
			elif differenceValue < 0:
				uValue = 0
				dValue = abs(differenceValue)
			else:
				uValue = 0
				dValue = 0
			U.append(uValue)
			D.append(dValue)
			sumU += uValue
			sumD += dValue

		## Ichikumo
		if iterator > kijun_value:
			number_of_kijun+=1
			if closeData > kijun_max:
				kijun_max = closeData
			if closeData < kijun_min:
				kijun_min = closeData
		if iterator > tenkan_value:
			number_of_tenkan+=1
			if closeData > tenkan_max:
				tenkan_max = closeData
			if closeData < tenkan_min:
				tenkan_min = closeData
		if iterator > senkou_value:
			number_of_senkou+=1
			if closeData > senkou_max:
				senkou_max = closeData
			if closeData < senkou_min:
				senkou_min = closeData
		
		iterator+=1
		previous_close_value = closeData

	## RSI Calculating
	# From https://www.macroption.com/rsi-calculation/
	numValues = len(U)
	smoothing_factor = 1/numValues
	currentAverageU = 0
	currentAverageD = 0
	previousAverageU = sumU/numValues
	previousAverageD = sumD/numValues
	for i in range(0, numValues-1):
		currentAverageD = smoothing_factor*D[i]+(1-smoothing_factor)*previousAverageD
		currentAverageU = smoothing_factor*U[i]+(1-smoothing_factor)*previousAverageU
		previousAverageU = currentAverageU
		previousAverageD = currentAverageD
	relative_strength = previousAverageU/previousAverageD
	RSI = 100 - (100 / (1+relative_strength))
	if RSI>=70:
		RSI = "{} (overbought)".format(RSI)
	elif RSI<=30:
		RSI = "{} (oversold)".format(RSI)



		



	## Kumo Calculating
	tenkan_sen = (tenkan_min+tenkan_max)/2
	kijun_sen = (kijun_min+kijun_max)/2
	senkou_span_A = (tenkan_sen+kijun_sen)/2
	senkou_span_B = (senkou_min+senkou_max)/2
	Kumo = senkou_span_A-senkou_span_B
	#print("Senkou Span A = {} ; Senkou Span B = {} ; Komu = {} \nnumber of Tenkan = {} ; number of Kijun = {} ; number of values = {}".format(senkou_span_A,senkou_span_B,Kumo,number_of_tenkan,number_of_kijun, number_of_data))

	return Kumo, RSI


def main(argv):
	# Credit : https://www.tutorialspoint.com/python/python_command_line_arguments.htm
	entry = ''
	outputfile = ''
	console = True
	mode = ''

	try:
		opts, args = getopt.getopt(argv,"cht:i:o:m:",["console","help","ticker=","ifile=","ofile=","mode="])
	except getopt.GetoptError:
		print('Usage : Bitpanda_Info_Parser.py -t <ticker> -i <full name> -o <output> -c <console output(default)>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('Usage : Bitpanda_Info_Parser.py -t <ticker> -i <full name> -o <output> -c <console output(default)>')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			entry = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
			console = False
		elif opt in ("-t", "--ticker"):
			entry = arg
		elif opt in ("-c", "--console"):
			console = True
		elif opt in ("-m", "--mode"):
			mode = arg
	if mode == '':
		print('Error : no input given')
		print('Usage : Bitpanda_Info_Parser.py -t <ticker> -i <full name> -o <output> -c <console output(default)>')
		sys.exit(2)
	else :
		data = getData(entry, mode)
	print("NAME = KUMO")
	print("{} = {}".format(entry, data))
	#print('mode : ',mode)
	#print('console output : ',console)
	#print('Data : ',data)

if __name__ == "__main__":
	main(sys.argv[1:])